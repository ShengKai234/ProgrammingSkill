class Soltion:
    def minDiffculty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        
        hardest_job_remaining = [0] * n
        hardest_job = 0
        for i in range(n - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job

        print(hardest_job_remaining)


if __name__ == '__main__':
    solution = Soltion()
    solution.minDiffculty([6,5,4,3,2,1], 2)