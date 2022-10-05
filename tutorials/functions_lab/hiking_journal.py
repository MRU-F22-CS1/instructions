def journal_entry(date: str, distance: float, message: str) -> str:
    """
    Takes a date, distance hiked, and message and forms a journal entry.
    Formats distance with one decimal place.
    """
    entry = f"On {date}, I hiked {distance:.1f} km.\n"
    entry = entry + message
    return entry

def main() -> None:
    """Main program entry point"""
    print("Journal Entry")
    journal_entry("July 12, 2022", 10.5, "I saw a beautiful lake.")

main()