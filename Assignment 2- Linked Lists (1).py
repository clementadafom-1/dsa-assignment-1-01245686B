"""Assignment 2: Linked Lists - University Helpdesk Ticket Queue."""


class Ticket:
    def __init__(self, ticket_id, student_name, issue):
        self.ticket_id = ticket_id
        self.student_name = student_name
        self.issue = issue
        self.next = None

    def __repr__(self):
        return (
            f"Ticket ID: {self.ticket_id}, "
            f"Student: {self.student_name}, "
            f"Issue: {self.issue}"
        )


class TicketQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue_ticket(self, ticket_id, student_name, issue):
        """Add a new ticket to the end of the queue."""
        new_ticket = Ticket(ticket_id, student_name, issue)

        if self.head is None:
            self.head = new_ticket
            self.tail = new_ticket
            return new_ticket

        self.tail.next = new_ticket
        self.tail = new_ticket
        return new_ticket

    def priority_insert(self, after_ticket_id, ticket_id, student_name, issue):
        """Insert a priority ticket immediately after a specified ticket ID."""
        current = self.head

        while current is not None:
            if current.ticket_id == after_ticket_id:
                new_ticket = Ticket(ticket_id, student_name, issue)
                new_ticket.next = current.next
                current.next = new_ticket

                if self.tail == current:
                    self.tail = new_ticket

                return True

            current = current.next

        return False

    def resolve_ticket(self, ticket_id):
        """Delete a resolved ticket by its ticket ID."""
        if self.head is None:
            return False

        if self.head.ticket_id == ticket_id:
            self.head = self.head.next

            if self.head is None:
                self.tail = None

            return True

        previous = self.head
        current = self.head.next

        while current is not None:
            if current.ticket_id == ticket_id:
                previous.next = current.next

                if self.tail == current:
                    self.tail = previous

                return True

            previous = current
            current = current.next

        return False

    def find_middle_ticket(self):
        """Find the middle ticket in one pass using fast and slow pointers."""
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_queue(self):
        """Reverse the queue in place by changing node pointers."""
        previous = None
        current = self.head
        self.tail = self.head

        while current is not None:
            next_ticket = current.next
            current.next = previous
            previous = current
            current = next_ticket

        self.head = previous

    def to_list(self):
        """Return all tickets as a list of tuples for testing and display."""
        tickets = []
        current = self.head

        while current is not None:
            tickets.append((current.ticket_id, current.student_name, current.issue))
            current = current.next

        return tickets

    def display_queue(self):
        """Print all ticket IDs and details in queue order."""
        if self.head is None:
            print("Queue is empty.")
            return

        current = self.head

        while current is not None:
            print(current)
            current = current.next


def run_tests():
    """Verify standard and edge cases for the ticket queue."""
    empty_queue = TicketQueue()
    assert empty_queue.find_middle_ticket() is None
    assert empty_queue.resolve_ticket(999) is False
    assert empty_queue.priority_insert(999, 1000, "None", "Missing ticket") is False
    empty_queue.reverse_queue()
    assert empty_queue.to_list() == []

    single_queue = TicketQueue()
    single_queue.enqueue_ticket(1, "Ama", "Password reset")
    assert single_queue.find_middle_ticket().ticket_id == 1
    assert single_queue.resolve_ticket(1) is True
    assert single_queue.to_list() == []

    queue = TicketQueue()
    queue.enqueue_ticket(101, "Isaac", "Password Reset")
    queue.enqueue_ticket(102, "Ama", "WiFi Connection Problem")
    queue.enqueue_ticket(103, "Kojo", "Printer Not Working")

    assert queue.priority_insert(102, 104, "Mary", "Exam Portal Access Issue") is True
    assert queue.to_list() == [
        (101, "Isaac", "Password Reset"),
        (102, "Ama", "WiFi Connection Problem"),
        (104, "Mary", "Exam Portal Access Issue"),
        (103, "Kojo", "Printer Not Working"),
    ]

    assert queue.resolve_ticket(103) is True
    assert queue.find_middle_ticket().ticket_id == 102

    queue.reverse_queue()
    assert queue.to_list() == [
        (104, "Mary", "Exam Portal Access Issue"),
        (102, "Ama", "WiFi Connection Problem"),
        (101, "Isaac", "Password Reset"),
    ]


def print_complexity_analysis():
    print("\nComplexity Analysis:")
    print("Enqueue ticket: O(1) time with a tail pointer, O(1) space")
    print("Priority insert: O(n) time, O(1) space")
    print("Resolve ticket: O(n) time, O(1) space")
    print("Find middle ticket: O(n) time, O(1) space")
    print("Reverse queue: O(n) time, O(1) space")
    print("Display queue: O(n) time, O(1) space")


if __name__ == "__main__":
    run_tests()

    queue = TicketQueue()
    queue.enqueue_ticket(101, "Isaac", "Password Reset")
    queue.enqueue_ticket(102, "Ama", "WiFi Connection Problem")
    queue.enqueue_ticket(103, "Kojo", "Printer Not Working")

    print("Initial Queue:")
    queue.display_queue()

    if queue.priority_insert(102, 104, "Mary", "Exam Portal Access Issue"):
        print("\nPriority ticket inserted after Ticket 102.")
    else:
        print("\nSpecified Ticket ID not found.")

    print("\nQueue After Priority Insert:")
    queue.display_queue()

    if queue.resolve_ticket(103):
        print("\nTicket 103 resolved.")
    else:
        print("\nTicket ID not found.")

    print("\nQueue After Resolving Ticket 103:")
    queue.display_queue()

    middle = queue.find_middle_ticket()
    print("\nMiddle Ticket:")
    print(middle if middle is not None else "Queue is empty.")

    queue.reverse_queue()
    print("\nQueue After Reversal:")
    queue.display_queue()

    print_complexity_analysis()
