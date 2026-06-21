class Ticket:
    def __init__(self, ticket_id, student_name, issue):
        self.ticket_id = ticket_id
        self.student_name = student_name
        self.issue = issue
        self.next = None


class TicketQueue:
    def __init__(self):
        self.head = None

    # 1. Enqueue Ticket
    def enqueue_ticket(self, ticket_id, student_name, issue):
        new_ticket = Ticket(ticket_id, student_name, issue)

        if self.head is None:
            self.head = new_ticket
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_ticket

    # 2. Priority Insert
    def priority_insert(self, after_ticket_id, ticket_id, student_name, issue):
        current = self.head

        while current:
            if current.ticket_id == after_ticket_id:
                new_ticket = Ticket(ticket_id, student_name, issue)

                new_ticket.next = current.next
                current.next = new_ticket

                print(f"Priority ticket inserted after Ticket {after_ticket_id}")
                return

            current = current.next

        print("Specified Ticket ID not found.")

    # 3. Resolve Ticket
    def resolve_ticket(self, ticket_id):

        if self.head is None:
            print("Queue is empty.")
            return

        if self.head.ticket_id == ticket_id:
            self.head = self.head.next
            print(f"Ticket {ticket_id} resolved.")
            return

        prev = None
        current = self.head

        while current:
            if current.ticket_id == ticket_id:
                prev.next = current.next
                print(f"Ticket {ticket_id} resolved.")
                return

            prev = current
            current = current.next

        print("Ticket ID not found.")

    # 4. Find Middle Ticket
    def find_middle_ticket(self):

        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # 5. Reverse Queue
    def reverse_queue(self):

        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        self.head = previous

    # 6. Display Queue
    def display_queue(self):

        if self.head is None:
            print("Queue is empty.")
            return

        current = self.head

        while current:
            print(
                f"Ticket ID: {current.ticket_id}, "
                f"Student: {current.student_name}, "
                f"Issue: {current.issue}"
            )
            current = current.next


# -----------------------------
# TESTING THE PROGRAM
# -----------------------------

queue = TicketQueue()

# Enqueue Tickets
queue.enqueue_ticket(101, "Isaac", "Password Reset")
queue.enqueue_ticket(102, "Ama", "WiFi Connection Problem")
queue.enqueue_ticket(103, "Kojo", "Printer Not Working")

print("Initial Queue:")
queue.display_queue()

# Priority Insert
queue.priority_insert(
    102,
    104,
    "Mary",
    "Exam Portal Access Issue"
)

print("\nQueue After Priority Insert:")
queue.display_queue()

# Resolve Ticket
queue.resolve_ticket(103)

print("\nQueue After Resolving Ticket 103:")
queue.display_queue()

# Find Middle Ticket
middle = queue.find_middle_ticket()

if middle:
    print("\nMiddle Ticket:")
    print(
        f"Ticket ID: {middle.ticket_id}, "
        f"Student: {middle.student_name}, "
        f"Issue: {middle.issue}"
    )

# Reverse Queue
queue.reverse_queue()

print("\nQueue After Reversal:")
queue.display_queue()