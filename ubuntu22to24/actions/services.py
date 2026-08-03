# Copyright 1999-2026. WebPros International GmbH. All rights reserved.

from pleskdistup.common import action, systemd


class SystemdReexec(action.ActiveAction):

    def __init__(self):
        self.name = "reexecute systemd"

    def _prepare_action(self) -> action.ActionResult:
        systemd.reexec_systemd_daemon()
        return action.ActionResult()

    def _post_action(self) -> action.ActionResult:
        return action.ActionResult()

    def _revert_action(self) -> action.ActionResult:
        return action.ActionResult()

    def estimate_prepare_time(self) -> int:
        return 1

