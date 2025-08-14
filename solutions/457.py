# tortoise and hare 
class Solution(object):
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue


            direction = nums[i] > 0
            slow, fast = i, i

            while True:
                next_slow = next_index(slow)
                if nums[next_slow] == 0 or (nums[next_slow] > 0) != direction:
                    break


                next_fast = next_index(fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break
                next_fast = next_index(next_fast)
                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break

                slow, fast = next_slow, next_fast

                if slow == fast:
                    if slow == next_index(slow): 
                        break
                    return True


            slow = i
            sign = nums[i] > 0
            while nums[slow] != 0 and (nums[slow] > 0) == sign:
                next_slow = next_index(slow)
                nums[slow] = 0
                slow = next_slow

        return False
