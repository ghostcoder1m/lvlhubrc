from sqlalchemy.orm import Session
from models import Workflow, Trigger, Action, WorkflowExecution, ActionExecution
from apscheduler.schedulers.background import BackgroundScheduler
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# Create a scheduler instance
scheduler = BackgroundScheduler()
scheduler.start()

def execute_trigger_actions(trigger_id: int, db: Session):
    """
    Executes actions associated with a given trigger.
    """
    try:
        trigger = db.query(Trigger).filter(Trigger.id == trigger_id).first()
        if not trigger:
            logger.error(f"Trigger with ID {trigger_id} not found.")
            return

        workflow = trigger.workflow
        if not workflow.is_active:
            logger.info(f"Workflow '{workflow.name}' is not active. Skipping execution.")
            return
        
        workflow_execution = WorkflowExecution(workflow_id=workflow.id, status="running")
        db.add(workflow_execution)
        db.commit()
        db.refresh(workflow_execution)

        logger.info(f"Executing actions for trigger: {trigger.type} with parameters: {trigger.parameters}")

        for action in trigger.actions:
            action_execution = ActionExecution(workflow_execution_id=workflow_execution.id, action_id=action.id, status="running")
            db.add(action_execution)
            db.commit()
            db.refresh(action_execution)

            # Implement action execution logic here
            # For example, if action.type == "send_email":
            #     send_email(action.parameters)

        workflow_execution.status = "completed"
        db.commit()

    except Exception as e:
        logger.exception(f"An error occurred while processing trigger job: {e}")
        if 'workflow_execution' in locals():
            workflow_execution.status = "failed"
            db.commit()

def schedule_trigger(db: Session, trigger: Trigger):
    """Schedules a single trigger based on its type and parameters."""
    try:
        if trigger.type == 'schedule':
            # Example scheduling logic for a daily trigger
            scheduler.add_job(
                execute_trigger_actions,
                'cron',
                hour=trigger.parameters.get("hour", 0),
                minute=trigger.parameters.get("minute", 0),
                args=[trigger.id, db],
                id=f"trigger_{trigger.id}",
                replace_existing=True
            )
            logger.info(f"Scheduled trigger: {trigger.type} with parameters: {trigger.parameters}")

    except Exception as e:
        logger.exception(f"Error scheduling trigger {trigger.id}: {e}")

def schedule_workflow_triggers(db: Session):
    """Loads all triggers from the database and schedules them."""
    try:
        triggers = db.query(Trigger).all()
        for trigger in triggers:
            schedule_trigger(db, trigger)
        logger.info("Workflow triggers scheduled successfully.")
    except Exception as e:
        logger.exception(f"Error scheduling workflow triggers: {e}")
