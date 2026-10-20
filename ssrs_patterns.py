
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


# 1. SINGLETON PATTERN
class SystemConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.system_name = "WUA SSRS"
        return cls._instance


# 2. FACTORY PATTERN
@dataclass
class ServiceRequest:
    reference: str
    student_id: str
    category: str
    description: str
    status: str
    created_at: str


class ServiceRequestFactory:
    @staticmethod
    def create(student_id, category, description):
        if not student_id.strip():
            raise ValueError("Student ID is required.")
        if not category.strip():
            raise ValueError("Category is required.")
        if not description.strip():
            raise ValueError("Description is required.")

        return ServiceRequest(
            reference=f"REQ-{uuid4().hex[:8].upper()}",
            student_id=student_id,
            category=category,
            description=description,
            status="Submitted",
            created_at=datetime.now().isoformat(
                timespec="seconds"
            ),
        )


# 3. OBSERVER PATTERN
class RequestStatusNotifier:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self, request, old_status, new_status):
        for observer in self._observers:
            observer(request, old_status, new_status)


def print_status_update(request, old_status, new_status):
    print(
        f"Request {request.reference}: "
        f"{old_status} -> {new_status}"
    )


# Demonstration
if __name__ == "__main__":
    config1 = SystemConfig()
    config2 = SystemConfig()
    print("Same config instance:", config1 is config2)
    print("System:", config1.system_name)

    request = ServiceRequestFactory.create(
        student_id="STU001",
        category="Maintenance",
        description="A classroom light is not working."
    )
    print("Created request:", request)

    notifier = RequestStatusNotifier()
    notifier.subscribe(print_status_update)

    old_status = request.status
    request.status = "In Progress"
    notifier.notify(request, old_status, request.status)
