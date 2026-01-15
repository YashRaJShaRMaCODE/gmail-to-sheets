from state_manager import load_state, save_state, is_processed, mark_processed

state = load_state()

test_id = "test-message-123"

if not is_processed(state, test_id):
    print("Message not processed. Marking now.")
    mark_processed(state, test_id)
    save_state(state)
else:
    print("Message already processed.")
