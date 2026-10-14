class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        desc=sorted(score, reverse=True)
        score_dict={}
        for i in desc:
            score_dict[i] = str(desc.index(i) + 1)
        for i in score_dict:
            if score_dict[i] == "1":
                score_dict[i]="Gold Medal"
            elif score_dict[i] == "2":
                score_dict[i]="Silver Medal"

            elif score_dict[i] == "3":
                score_dict[i]="Bronze Medal"
        output=[]
        for i in score:
            output.append(score_dict[i])
        return output
        