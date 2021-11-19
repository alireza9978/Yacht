from algorithms.Statistics import *
from utils.SaveFile import *

if __name__ == '__main__':
    state_list = create_all_state()
    state_file = generate_unique_state_count(state_list)
    save_csv(state_file, "unique_states_info")
