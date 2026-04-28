# Explaining recommendation systems through contrapositive perturbations

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Recommender systems are widely used to help users discover new items online. A popular method for recommendations is factorization models, which predict a user's preference for an item based on latent factors derived from their interaction history. However, explaining why a particular item was recommended to a user is challenging, and current approaches such as counterfactual explanations can be computationally expensive. In this paper, we propose a new approach called contrapositive explanations that leverages a different logical structure to counterfactual explanations. We show how contrapositive explanations can be used to explain recommendation systems by finding the minimum change that would have resulted in a different recommendation. Specifically, we present a methodology that focuses on finding an explanation in the form of "Because the user interacted with item, j we recommend item i to the user," which is easier to compute and find compared to traditional counterfactual approaches which aim at "Because the user $\textbf{did not}$
 interacted with item j, we $\textbf{did not}$ recommend item i to the user,". We evaluate our approach on several real-world datasets and show that it provides effective and efficient explanations compared to other existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an interesting explanation method to explain recommendation systems through contrapositive perturbations, leveraging the key insight that (negation of B => negation of A) and (A=>B) are equivalent . The proposed method is computational efficient to SVD and MLP-based recommender systems. Lastly, the paper evaluates the approach against benchmarks on several datasets to demonstrate its effectiveness and efficiency in explanations. 

The approach seems novel and interesting but have some questions and concerns on the experimentation session.  Mostly concern if the paper is comparing to the compelling baselines, and M_contra seems to on part to "influence" functions in some datasets:
Q1: do we have compelling baselines to compare against? The reason asked is because if we comparing item similarity and influence comparing to random, they seem to be not very statistically different in M_contra in many cases (i.,e, Figure 2 on Dimension 32 for # of expl Q2:  in Figure 4, it seems that "Influence" is comparable or have higher M_contra value as "Contrapositive" approach in Dataset ML-100k, is that expected?

### Strengths
The paper proposes an interesting explanation method to explain recommendation systems through contrapositive perturbations, leveraging the key insight that (negation of B => negation of A) and (A=>B) are equivalent . The proposed method is computational efficient to SVD and MLP-based recommender systems. Lastly, the paper evaluates the approach against benchmarks on several datasets to demonstrate its effectiveness and efficiency in explanations.

### Weaknesses
Mostly have some concern and/or questions on the Experiment session if the paper is comparing to the compelling baselines.
Q1: do we have compelling baselines to compare against? The reason asked is because if we comparing item similarity and influence comparing to random, they seem to be not very statistically different in M_contra in many cases (i.,e, Figure 2 on Dimension 32 for # of expl Q2:  in Figure 4, it seems that "Influence" is comparable or have higher M_contra value as "Contrapositive" approach in Dataset ML-100k, is that expected?

### Questions
Mostly have some concern and/or questions on the Experiment session to prove out on the claims. 
Q1: in Figure (2) and (3), as the number pf experiments increase, in particular at 5, it seems that the contrapositive approach is non-stats sign from other baselines, especially Item Similarity or Influence. Was this the expected behavior?  
Q2: in Figure 4,  it seems that "Influence" is comparable or have higher M_contra value as "Contrapositive" approach in Dataset ML-100k, is that expected.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper is trying to address the challenge of explaining recommendations, which is meaningful and important because recommender systems like factorization models based or neural network based are lack of transparency. The paper introduces a novel approach called "contrapositive explanations (Contra+)" to provide clear and efficient explanations for recommendations. Contra+ focuses on finding explanations in the form of "Because the user interacted with item j, we recommend item i to the user." This is in contrast to traditional counterfactual explanations, which aim to explain why an item was not recommended. This paper provides detailed discussion for previous methods, many toy examples and figures to make the concepts easier for readers to understand. Finally, the authors demonstrate the effectiveness and efficiency of Contra+ through empirical experiments on real-world datasets.

### Strengths
S1: This paper considers a interesting questions (explaining recommendation system) from a contrapositive perspective, which is novel.

S2: This paper provides detailed discussion for previous methods, many toy examples and figures to make the concepts easier for readers to understand.

S3: This paper gives a comprehensive review of differences and similarities between contrapositive and counterfactual explanations.

### Weaknesses
W1: The key concern is whether there is another way to get the "explanation". Further, is there an infinite number of ways to perturb the embedding that can achieve the same purpose, i.e., "We did not recommend item i to user u"? In such case, does each way of perturbing the embedding correspond to a different h, i.e., "User u would not have interacted with item h"? How can we distinguish the merits and drawbacks of each perturbation? It's unclear if the proposed method is finding a unique or optimal explanation, or just one of many possibilities, and how the choice of perturbation affects the quality of the explanation.

W2: Previous literature like Tan et al. [1], studied cause on a particular aspect, i.e., If the item had been slightly worse on [aspect(s)], then it will not be recommended. This can find the cause on a particular aspect, whereas in this paper, the cause is found on perturbation on all embedding. Is there any comment on the difference? The paper does not adequately address the potential benefits of aspect-specific perturbations, which could provide more targeted and interpretable explanations.

W3: The authors give a lot of toy examples, such as rain and slippery roads, or godfather and godfather 2. Can some experiments be added to give some examples of real-world datasets where the proposed method finds an explanation? For example, in Netflix or ML-1M, are there any cases where users don't interact with "computer" because "cell phone" is not suggested? The lack of real-world examples makes it difficult to assess the practical relevance of the explanations.

W4: Counterfactual explanations don't necessarily guarantee removing the explanation or changing the recommendation. Therefore, in figure 1, counterfactual explanations should be 1 as a proportion of all areas, that is, 1/(1+2+3+4), not 1/(1+2). The current calculation of the counterfactual metric in Figure 1 is misleading and does not accurately represent the proportion of cases where a counterfactual explanation would actually change the recommendation.

W5: The experiment process is Evaluations part is not so clear. For example, why is $M_{contra}$ greater than 1? In addition, consider doing some runtime experiments and some other hyper-parameter sensitivity analysis or in-depth analysis like the effect of varying total amount data could be better. The experimental evaluation lacks clarity and depth, with insufficient detail on the metrics used and a lack of analysis on the computational cost and sensitivity to hyper-parameters.

### Questions
Please refer to the weaknesses part for the questions.

=== AFTER REBUTTAL ===

I thank the authors for taking the time to answer my questions, which addresses some of my concerns. However, I still have some concerns about the motivation and methodology. Hence, I may maintain my score.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the interpretability problem “because the user interacted with item $j$, we recommend item $i$ to the user” in a factorization model commonly used in recommender systems. From the perspective of contrapositive logit (“because the user did not interact with item $j$, we did not recommend item $i$ to the user”), this paper proposes a new explanation algorithm (Contra+) consisting of two steps: (1) perturbing the user embedding to ensure item $i$ is not recommended; (2) given the perturbed user embedding, identifying the historical items that have lost most relevance to the user. Overall, the proposed algorithm is interesting but is more empirical and lacks theoretical guarantees.

### Strengths
1. the writing is well and the presentation is clear.

2. the topic is interesting.

### Weaknesses
1. the proposed method is more empirical and lacks theoretical guarantees (see main question 1 for more details).

2. something about the key logic of the algorithm is not clearly explained (see main question 2 for more details).

### Questions
**Main Questions**

1.	the perspective of contrapositive logit is not fully novel. In fact, Pearl (1999)[1] defined the notation of **probability of necessary causation**, which follows the same logic as contrapositive. There may be some connection between the probability of necessary causation and the method proposed in this paper. Linking the method proposed in this paper with the necessary causality probability may provide a theoretical guarantee for the method proposed in this paper. Could you discuss something about the possible connections?

2.	Here are some questions about the key logic of the proposed method.

>(1) In terms of the perturbation, (a) Why only the user embedding is perturbed and not the item embedding? It is a bit confusing to me. intuitively, the user after the perturbation is no longer the same user before. (b) Do all user-item pairs, using the same strength ($\gamma$ and $\epsilon$ in equation (4)) of perturbation? (c) How to choose the parameters $\gamma$ and $\epsilon$ in practical applications?

>(2) For step 2, i.e., identifying the historical items that have lost most relevance to the user. Why the historical items that have lost the most relevance to the new perturbed user embedding is the explanation? Is it equivalent to the statement “because the user did not interact with item $j$, we did not recommend item $i$ to the user”? 

[1] Judea Pearl (1999), Probabilities of causation: three counterfactual interpretations and their identification.


**Minor Questions**

(1)	There are some problems with the format of the citation. For example, at the end of the first paragraph in the Introduction, the citation format should appear as (Lu et al., 2012; Aggarwal et al., 2016; Beel et al., 2016; Jannach et al., 2022), which can be generated using the \citep{XXX} command.

(2)	There are some grammatical errors. For example, at the end of the Abstract, “… because the user did not **interacted** with item $j$ ….” should be  “… because the user did not **interact** with item $j$ ….”.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
