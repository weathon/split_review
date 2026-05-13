# Stable batched bandit:  Optimal regret with free inference

- Decision: Reject
- Scores: 3, 3, 5, 5, 5

## Abstract
In this paper, we discuss statistical inference when using a sequential strategy to collect data. While inferential tasks become challenging with sequentially collected data, we argue that this problem can be alleviated when the sequential algorithm satisfies certain stability properties; we call such algorithms stable bandit algorithms. Focusing on batched bandit problems, we first demonstrate that popular algorithms including the greedy-UCB algorithm and $\epsilon$-greedy ETC algorithms are not stable, complicating downstream inferential tasks. Our main result shows that a form of elimination algorithm is stable in the batched bandit setup, and we characterize the asymptotic distribution of the sample means. This result allows us to construct asymptotically exact confidence intervals for arm-means which are sharper than existing concentration-based bounds. As a byproduct of our main results, we propose an Explore and Commit (ETC) strategy, which is stable --- thus allowing easy statistical inference--- and also attains optimal regret up to a factor of 4.

Our work connects two historically conflicting paradigms in sequential learning environments: regret minimization and statistical inference. Ultimately, we demonstrate that it is possible to minimize regret without sacrificing the ease of performing statistical inference, bridging the gap between these two important aspects of sequential decision-making.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Summary:
The problem studied is to design multi-armed bandit algorithms for stochastic bandit problems 
so that the central limit theorem (CLT) holds for the rewards collected for each of the arms in the limit of infinitely many interactions. Let's call a bandit algorithm CLT friendly if it satisfies this criterion.

The notion of "stability" of bandit algorithms is introduced. According to this definition, a bandit algorithm is stable, if for any bandit instance of interest, there exist deterministic sequences $\{ n_{a,t} \}$ such that $\frac{N_{a,t}}{n_{a,t}}$ converges to one in probability where $N_{a,t}$ is the number of pulls of arm $a$ up to round $t$ on the given instance (a random quantity).
A simple calculation shows that stable bandit algorithms are CLT friendly.
The authors also show that ETC (explore for, say, half the time, then choose the better arm out of, say, two) is not stable. They also cite previous research that shows that ETC is not "CLT friendly", which indicates that enforcing stability may be necessary for CLT friendliness.
Then they design an ETC-style method, which explores in the first phase, but then instead of choosing greedily, uses confidence bounds with the data of the first phase to eliminate arms. If multiple arms remain, the algorithm splits the remaining time equally between them (the authors use randomization for this). If a single arm remains, that arm is pulled up to the end. This algorithm is shown to be stable.

Significance: The problem is not entirely new, several authors looked into CLT friendliness previously. This reviewer is not completely sold on this notion: CLT is truly asymptotic, it is unclear what this notion really buys for practice if anything. Also CLT friendliness could be achieved easily if we did not demand to use all rewards from all the arms: just allocate a fixed, even diminishing portion, of all time steps to uniformly exploring the arms and use the rewards collected during this period. The results of this paper are not strong enough to discard an algorithm like this on reasonable grounds. In other words, not much depth is achieved in the paper.

Novelty: The notion of stability is novel. The proofs are quite standard/automatic (even though I am not completely happy with how, e.g., the proof of Theorem 1 is done).

Related work: Somehow the authors want to connect this to batched bandits, but at least the main paper did not do much with this. The algorithm presented for the batched case with B cases raises more questions than it answers (maybe a presentation issue).

Soundness: I think the claims made are correct. I verified things to a reasonable degree in the main text.

Presentation:  There are a number of typos, grammatical issues (e.g., line 155: "We assume Let ...", line 158: genrality, etc.) I will list a few more of these at the end. In the algorithms, the authors use "or", but this should be "otherwise" (last line of all algorithms). This was very confusing. Also, the proof of Theorem 1 is quite messy (one of the two proofs in the main body). The authors state "It suffices to study the behavior of $n_{1,T}$ on the high probability event $\mathcal{E}_T$". Why? In what sense? (Later we find out, but this is not the sign of a well written text.) Also, only in the middle of the proof we find out that there will be two cases based on the value of $\beta$. This proof definitely can use polishing, as can the rest of the paper.

### Strengths
The paper does make novel contributions.

### Weaknesses
I did not find the topic well motivated. The paper feels weak on contributions: A strong paper would study the tradeoff between CLT friendliness and performance; nothing of this form is attempted here. The results, while they appear to be correct, do not require much effort. The batch bandit version of the algorithm is, hmm, unexpected, specifically in how it only uses data from the current batch, discarding the effect of previous batches. This raises concerns about its practical effectiveness as a bandit method. The presentation is poor; it feels that the paper needs much work, with numerous typos and grammatical issues. For example, line 155 states "We assume Let ...", and line 158 has "genrality". The use of "or" instead of "otherwise" in the algorithms is confusing, and the proof of Theorem 1 is quite messy and difficult to follow.

### Questions
It seems that in the batch bandit version of the algorithm in every batch, only data for that batch is used. The effect of previous batches is discarded. At least this is how the algorithm seems to be defined. While this may make the method CLT friendly, this will be a very bad bandit method. What is the point here?

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work explores statistical inference under sequentially and adaptively collected data. The authors focus on the batched bandit setting and show that ETC type policies are poor with inference due to lack of a property called "stability". They show that a form of Successive Elimination algorithm achieves stability and have good asymptotic inference properties as well as optimal regret bounds. They also generalize their results from the 2-batched setting to a multi-batched setting.

### Strengths
The context is relatively easy to follow. The problem considered is interesting.

### Weaknesses
Though this paper investigates an interesting and important problem, I am afraid the preprint is far from being ready for publish.

1. Contribution. What I am very confused is you contribution.
- You mention in the abstract you show that popular algorithms including the greedy-UCB algorithm and $\epsilon$-greedy ETC algorithms are not stable. Maybe I missed it, but where is it in the main context? Seems you only show the instability of the simple $\epsilon$-greedy ETC. The short argument on Line 268-269 seems to be very vague and built entirely on Zhang et al. (2020).
- You mention it is possible to minimize regret without sacrificing the ease of performing statistical inference. I think this is an overclaim. Your regret rate is in a non-asymptotic sense, but your inference task is in an asymptotic sense. Convergence in probability is a relatively weak measure --- it is a point-to-point convergence and one does not know the convergence rate. Also, in your result you show a sacrifice of factor $4$ in the regret bound.
- More importantly, it is very unclear how your work should be placed compared to Khamaru & Zhang (2024) which you also cited in the proof section. Khamaru & Zhang (2024) revisited the stability property, gave a detailed investigation of the asymptotic statistical properties of standard UCB. They also investigated the multi-armed setting (the number of arms $K$ can even be scaling with $T$). 
  - Can you elaborate on your additional contribution? Stability is not new. The algorithms (ETC and Elimination) are not new. The results seems to be similar (or maybe even weaker) compared to those from Khamaru & Zhang (2024).
  - Also, it seems the technical tools are largely following the literature. Is there any intrinsic difficulty within (a) studying Elimination rather than UCB and (b) studying the batched setting?

2. Writing. The writing of this paper is relatively poor.
- The results and proofs are written in a rather arbitrary way. Some gave a partial proof with equations, some invoked other works directly, while some simply mentioned that "a careful look at the proof reveals that one can replace ...". The content is indeed easy to follow, but the reading experience is not good.
- In Theorem 1 you are taking $m$ and $T$ to $+\infty$ such that $T-2m$ goes to $+\infty$. But in Theorem 2 the scaling of $m$ is unclear. Seems there is no? There are also many typos in the paper. For example, in both Theorem 1 and 2, the empirical variance term is in the wrong place; in Line 796-797, the equation after "the fact" is strange and contents after "Recall" are not in math format; the usage of ∴ is not formal. 
- There is only a small simulation example at the beginning of the paper. I understand the paper is focusing on theory, but since you claim you propose new algorithms (which are not hard to implement), it is anticipated that more comprehensive experiments should be conducted.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors introduce a class of algorithms known as "stable bandit algorithms" in which classical statistical methods used for iid data can be used for inference. Most of the results and discussion in the main paper is for 2 arm bandit setting, and this case, the authors show that the CLT holds for the sample means of the arms. The authors also show that the vanilla epsilon greedy explore-then-commit algorithm does not satisfy the stable bandit setting, and further go on to show that the sample means of the arms arms in this strategy does not satisfy the CLT. As a subsequent step, the authors propose a modified version of the algorithm that does belong to the class of stable bandit algorithms, and prove that its regret is asymptotically optimal (upto a constant factor). The authors also introduce another another algorithm "B-batch algorithm" that is also shown to be stable, and have nice asymptotic properties of the sample means of the arms.

### Strengths
In my opinion, the strength of the paper is how simple and elegant the theory is. It's nice to see that simple bandit algorithms that require such little computations have nice statistical properties.

### Weaknesses
1. I do not fully understand the motivation of the results. The authors claim "bridging gap between statistical inference and minimizing regret" but I do not understand what they mean by that exactly -- can the authors provide more concrete examples on how they do this? They discuss how previous analysis use "Martingale structure" in sequentially collected data for analysis, but so what? Specifically, what are the limitations of using martingale-based concentration inequalities for inference in the context of bandit algorithms, and why is asymptotic normality a superior alternative in certain scenarios? The authors should clarify the specific statistical challenges that arise when using standard bandit algorithms for inference and how their approach addresses these challenges.

2. I also don't understand what these results lead to in the practical / theoretical sense. The only future work the authors discuss is extension to K arm bandit setting: Can the authors provide specific examples of practical applications or theoretical implications of their results. How can stable bandit algorithms be applied in real-world scenarios? For instance, are there specific domains where the ability to obtain asymptotically normal sample means is particularly advantageous? The authors should provide concrete examples of how their results can be used to improve decision-making or analysis in practical settings. The authors mention "many" of the results in the paper extend to K-arm bandit settings, but which ones? I did not see any discussion on this topic -- the authors should let us know how the results extend to K-arm settings, and also the implications.

3. I don't know why these results are complex / novel -- could the authors explain why this analysis is special in the context of bandit literature? What are the key challenges in proving asymptotic normality for bandit algorithms, and how do the authors' techniques overcome these challenges? The authors should clearly articulate the specific technical contributions of their work and how they advance the state-of-the-art in bandit theory. It's not clear what makes this analysis different from standard asymptotic analysis of sample means, and why the bandit setting introduces additional complexities.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper considers the problem of statistical inference in context of sequentially / adaptively collected (and hence non-i.i.d.) data as arising in the multi-armed (batched) bandit setting.  In particular, the authors introduce a notion of stability for bandit algorithms, and prove that under their stability condition, sample means for arms are asymptotically normal, which allows the construction of valid confidence intervals.  They show that a commonly considered, simple explore-then-commit (ETC) strategy is unstable (and indeed yields non-normal reward means). They then provide a stable alternative, which, in the first stage, samples arms equally often, and in the second stage samples all plausibly optimal arms equally often. They also provide variants of this scheme, with adaptively selected duration of the first stage (which yields an algorithm with optimal asymptotic minimax regret up to a constant of 4), or with multiple stages of fixed length.

### Strengths
I very much appreciate the perspective for analysing multi-armed bandits using the lens of stability. While stability has been known to imply generalisation bounds in classical learning theory, its application to the analysis to bandits I had not seen before.  I could imagine it becoming a fruitful direction for future research in this area.  The fact that stability allows treating the data as effectively generated i.i.d. is potentially impactful.  The paper is generally clearly written (albeit there’s a number of typos).

### Weaknesses
While very interesting conceptually, the submission only considers a rather restricted setting:  A variant of batched bandits with two arms only.  While in Section 2, the authors claim that “many” of their results generalise to the K-armed setting, no further information is provided (which results? How do the results generalise?), and in Section 5, they mention the extension to the K-armed case as interesting future work.  In my opinion, stability would become a much more interesting concept if the results could be generalised to richer families of bandit instances, e.g., bandits with structured reward functions (e.g., linear bandits).  Besides the limitation to two arms, all presented results are only asymptotic in nature.  Thus, the work appears a bit preliminary for me.

Another, and perhaps more severe, concern is with the novelty of the presented framework.  The authors cite a paper entitled “Inference with ucb”.  Aiming to understand the relative contributions of the present submission, I found an article with the title “Inference with the upper confidence bound algorithm” on arXiv (https://arxiv.org/pdf/2408.04595).  This paper appears to introduce the same notion of stability for bandit algorithms and uses it to analyse the upper-confidence bound (ucb) bandit algorithm (in fact, Lemma 1 appears to be shown in that paper as well).   The paper appears to provide the same general conclusion (i.e., under stability, data can be effectively treated as i.i.d.) as in the ICLR submission.  The main difference appears to be that an analysis is presented for a different family of bandit algorithms (ucb).  With respect to this paper, the ICLR submission looks rather incremental, even more so in light of the rather restricted setting (as argued above).

The manuscript has a number of typos (here’s some of them):
- 60: maybe -> may be
- 158: genrality
- 224: on consistent estimator of
- 286: pull both arm

### Questions
- Can you please clarify, in your view, the relation and relative contribution to the paper https://arxiv.org/pdf/2408.04595?
- Can you please elaborate on whether there are meaningful connections to generalisation bounds obtained from stability in classical learning theory [cf. A,B]?  
- Section 2 makes the claim that “many” results generalise to the K-armed setting.  Which results?  And how do they generalise?
- \sigma_{a,T} as used, e.g., in line (10) seems to refer to the variance, in (11) it seems to be used as standard deviation.  Can you please clarify?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Given a set of arms and a bandit algorithm that collects data, this paper aims to understand the asymptotic properties of the empirical mean of each arm observed by running the algorithm. The focus is on the setting of 2 arms. While existing methods do not typically use information about the algorithm itself, this paper takes an algorithm-dependent approach, via the notion of stability (defined in Section 3.1). In particular, for stable algorithms, the empirical means are asymptotically normal (Lemma 1). This means that one can readily construct confidence intervals for the true means.

The paper discusses two types of algorithms: 2-batch and $B$-batch. For the former, they show that a vanilla $\epsilon$-greedy Explore Then Commit (ETC) strategy is not always stable (Lemma 2). They then modify the algorithm into a stable ETC variant (Algorithm 1); its stability is proved in Theorem 1. In both of these algorithms, the learner explores for a fixed number $\sim m$ of rounds and subsequently acts greedily. The authors then devise Algorithm 2, where they replace $m$ with a random stopping time. They then show that Algorithm 2 is stable (Corollary 2) and has asymptotically optimal regret, up to constants.

Lastly, they study a $B$-batch procedure. Algorithm 3 pulls each arm $\sim m$ times in each one of $B$ batches. Theorem 2 then shows that this algorithm is stable (when $m$ is fixed and $B\to\infty$).

### Strengths
- Overall, the paper is well-structured and clear, but would benefit from some clarifications (addressed below).

- It is an interesting approach to show asymptotic normality based on properties of the algorithm. 
    
- I think asymptotic normality is indeed important to be able to do inference on the arms (e.g., construct confidence intervals).

- The algorithms are relatively clear and simple to understand.

### Weaknesses
 - The 2 arm assumption is fairly limited. It might be productive to discuss how this can be extended, or at least acknowledge the limitations in the conclusion. The current analysis and algorithms are tailored to this specific case, and it is unclear how well they would generalize to more realistic scenarios with a larger number of arms.

- The paper would benefit from additional intuition on some concepts, such as (i) the definition of stability and (ii) the ratio in the constraint on $m$ of Equation (7). The definition of stability, while mathematically precise, lacks a clear explanation of why it is a relevant property for ensuring asymptotic normality. Similarly, the specific form of the constraint on $m$ (related to the exploration phase) needs more justification. Why is this particular ratio of $8\log T / \delta^2$ important, and what does it represent in terms of the algorithm's behavior?

- In Section 3.1, the authors should define $z_\alpha$. It is a standard notation, but for completeness, it should be defined explicitly for the reader. 

- In Corollary 2, the authors should define regret. The statement of the corollary mentions asymptotic optimality in terms of regret, but the term is not defined anywhere in the paper, making it difficult to assess the significance of the result.

- In Theorems 1 and 2, in the convergence in distribution to the Gaussian, shouldn't the LHS be dividing by $\hat\sigma_{a,T}$ instead of multiplying? The current formulation seems incorrect, as it would imply that the variance increases with the sample size, which is counterintuitive.

### Questions
- Is there a reason why in Algorithm 3, provided $\mathcal{A}_{b}$ contains both arms, we pull each one exactly $m$ times as opposed to the other algorithms, where we pull each one with probability $1/2$?

- How do you think the analysis for $K$ arms would work? Would it be a simple extension, or require more sophisticated techniques?

### Soundness
3

### Presentation
2

### Contribution
2
