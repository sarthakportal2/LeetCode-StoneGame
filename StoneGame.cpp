class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        //min. runtime(0 ms) S(C(N)=(O(1))) and (T(C(N)=O(n))due to Level wise iteration and requires non additonal space
        int n;int sum1=0;//variables declare and sum initization
        for(int i=0;i<piles.size();i++){//iterating to Pile's length
            if(piles[i]==0)return 0;//piles initizlation 
            else if(n%2==0 && n>0)return false;//prinitng false to   at  even stones piles positive number non winning condition 
            else if(piles[i]>0) piles.begin()=piles.end();return true;//printing true to the winner from piles begin till end at its most number
        }return false;}};//printing false for nonwining cond
    
