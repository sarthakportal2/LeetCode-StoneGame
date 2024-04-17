class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        #T(C(N)=O(N)) and S(C(N))=O(1) as it requires non memory space allocation iteratively 
        n=int()#Stone(n) declare
        for i in range(len(piles)):#iterating Through Pile's Stack's Length
            if piles[i]==0:return None#Initilaizing Pile
            elif n%2==0 and n>0:return False#Printing False to the Pile's Even Number of Stones
            elif piles[i]>0:piles[i]=piles[i-1];return True#printing True to Winner with the Pile's Start till its End  Odd Number Stone 
        return False#printing False to the Unwinner 
    #def stoneGame(self, piles: List[int]) -> bool:return True
