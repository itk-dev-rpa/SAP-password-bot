"""This module contains the main process of the robot."""

import os
import secrets

from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection
from itk_dev_shared_components.sap import sap_login


def process(orchestrator_connection: OrchestratorConnection) -> None:
    """Do the primary process of the robot."""
    orchestrator_connection.log_trace("Running process.")

    credential_names = orchestrator_connection.process_arguments.split(",")

    for name in credential_names:
        orchestrator_connection.log_info(f"Changing password for {name}.")

        cred = orchestrator_connection.get_credential(name)

        new_password = create_password()

        sap_login.change_password(username=cred.username, old_password=cred.password, new_password=new_password)

        orchestrator_connection.update_credential(name, new_username=cred.username, new_password=new_password)

    orchestrator_connection.log_info(f"Changed {len(credential_names)} passwords.")


def create_password() -> str:
    """Generate a 16 length password containing [A-Z][a-z][_-].

    Returns:
        A random 16 length string.
    """
    return secrets.token_urlsafe(16)[:16]


if __name__ == '__main__':
    conn_string = os.getenv("OpenOrchestratorConnString")
    crypto_key = os.getenv("OpenOrchestratorKey")
    oc = OrchestratorConnection("Password Test", conn_string, crypto_key, "")
    process(oc)
