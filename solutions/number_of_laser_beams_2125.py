class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """

        lasers = 0 
        prev_level_count = 0 

        # check where the lasers are 
        for i in range(len(bank)): 
            level_count = 0 
            for j in range(len(bank[0])): 
                if bank[i][j] == "1": 
                    level_count += 1 

            if level_count != 0: 
                # the number of lasers is this formula 
                lasers += (prev_level_count * level_count) 

                # update for the next level 
                prev_level_count = level_count 
    
        return lasers 


        
