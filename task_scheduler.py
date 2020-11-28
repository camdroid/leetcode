class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = {}
        uniqueTasks = set(tasks)
        frequencies = {t: tasks.count(t) for t in uniqueTasks}
            
        # frequencies of the tasks
        frequencies = list(frequencies.values())

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)

