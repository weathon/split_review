# A Large-Scale Analysis on Methodological Choices in Deep Reinforcement Learning

- Decision: Reject
- Scores: 6, 3, 6, 3, 3

## Abstract
Deep reinforcement learning research has been the center of remarkable scientific progress for the past decade. From winning one of the most challenging games to algorithmic advancements that allowed solving problems without even explicitly knowing the rules of the task at hand reinforcement learning research progress has been the epicenter of many breakthrough ideas. In this paper, we analyze the methodological issues in deep reinforcement learning. We introduce the theoretical foundations of the underlying causes outlining that the asymptotic performance of deep reinforcement learning algorithms does not have a monotone relationship to the performance in the regimes where data becomes scarce. The extensive large-scale empirical analysis provided in our paper discovers that a major line of deep reinforcement learning research under the canonical methodological choices resulted in suboptimal conclusions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
One commonly studied benchmark is the Atari 100K benchmark in which algorithms are evaluated in low sample complexity regimes. Distributional variants of RL algorithms have shown high performance in the high data regime and have been transferred over to the low data regime of Atari 100K. This paper investigates the differences across different data regimes both from a theoretical and empirical perspective. There are two main theoretical results. The first shows that results are non-monotonic across regimes, and the second investigates the difficulties of learning distributions (e.g., in distributional RL). The empirical results show how distributional variants underperform non-distributional variants in the low-data (Atari 100K regime), which has implications for prior work in the literature that may have overlooked the impact of distributional RL.

### Strengths
I think this paper is decently written from a didactic point of view. The work itself does appear to be novel, both in terms of theory and experiments. The theoretical results on the data regimes and distribution learning seem interesting, insightful, and non-vacuous.  I think the community would be interested in these results, as they a) have implications for algorithm design and selection dependent on the data regime, and b) contain novel insights about several popular and well-cited algorithms for the Atari 100K benchmark. The experiments indeed serve to demonstrate the authors' point and are, by my assessment, sufficient.

I have mentioned several weaknesses. I might have given a higher score if these weaknesses were not present. I think this paper is acceptable because it has useful insights that are shown clearly, but there are flaws with the writing and paper itself that suggest that the work at present is not ready.

### Weaknesses
- The paper does not clearly state what the canonical methodological choices are. For a study titled "A LARGE-SCALE ANALYSIS ON METHODOLOGICAL
CHOICES IN DEEP REINFORCEMENT LEARNING", it is not clearly stated anywhere. Considering this is large-scale analysis of choices, I wonder what other choices are being investigated (e.g., outside of distributional learning). Figure 1 has "instances of methodological choices", but it's a bit unclear how algorithms are methodological choices. Clarity here would help.
- I did feel as though the question: "(i) What are the canonical methodological choices that fundamentally effects the progress in deep reinforcement learning research" was not adequately addressed or studied in the paper. In fact, they were not even listed.
- The paper lacks a related work section. This is fine per se, but there is no part of the paper that discusses the extent to which these insights are or not studied in prior work.

- Typo: "(i) What are the canonical methodological
choices that fundamentally effects the progress in deep reinforcement learning research" 
	- "effects" -> "affects"

### Questions
- Given that the paper's title is "A LARGE-SCALE ANALYSIS ON METHODOLOGICAL
CHOICES IN DEEP REINFORCEMENT LEARNING", can you please list out all the methodological choices that were investigated?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates the methodological approaches commonly adopted in deep reinforcement learning (DRL) and challenges several prevalent assumptions. The authors argue that many DRL studies implicitly assume that an algorithm's performance in high-data settings (where ample training data is available) will predict its performance in low-data settings (where data is limited). Authors claim that this assumption has led to methodological biases and suboptimal conclusions in the field. The study highlights that common methodological choices in DRL, particularly the assumption of a monotonic relationship between high-data and low-data performance, are flawed. 

Through theoretical analysis and empirical testing, the paper demonstrates that performance profiles of DRL algorithms do not maintain a simple, predictable relationship between data regimes. Algorithms optimized for high-data performance do not necessarily perform well with limited data, and vice versa. The authors provide theoretical proofs and empirical results showing that simpler algorithms, such as the dueling network architecture, can outperform more recent methods in low-data scenarios.

Large-scale experiments on the Arcade Learning Environment (ALE) reinforce the theoretical findings, showing that simpler, established algorithms often outperform newer, more complex approaches under limited data conditions. The paper advocates for including these simpler baselines in performance comparisons to provide a more accurate picture of algorithm efficacy.

### Strengths
**Strengths:**

1) The paper presents a large-scale empirical analysis across multiple algorithms and data regimes, using the Arcade Learning Environment (ALE) benchmark.

2) In addition to empirical findings, the paper includes thorough theoretical analysis. The proofs related to non-monotonic performance across data regimes are well-founded and add a layer of depth to the study. 

3) The authors identify and explain methodological biases resulting from high-data assumptions.

### Weaknesses
 **Potential weaknesses:**

1) The empirical analysis is heavily focused on the Arcade Learning Environment (ALE), which, while popular, may not fully represent the broader range of tasks and environments encountered in deep reinforcement learning. A more diverse set of benchmarks, such as continuous control tasks or real-world scenarios, could make the conclusions more generalizable.
While the authors advocate for a paradigm shift in evaluating DRL algorithms, the paper does not discuss how its findings could be applied in practice. For instance, guidelines on designing experiments or adjusting evaluation metrics to avoid high-data biases would make the recommendations more actionable for researchers.

2) A recent paper has highlighted the phenomenon of data regime issues, offering valuable insights and prompting a reformulation of the research question in the paper [1].

3) I do not think it is accurate to say that algorithms developed for Atari100k (Data Efficient RL) are compared with those developed for Atari 200M (high-data regime) [2, 3, 4]. Please check the section "Case Study: The Atari 100k benchmark" in [5].

4) I believe the main takeaway of the paper is incorrect. It is clear that agents that perform well in the large data regime do not necessarily perform well compared to those developed for Atari100k. DER is essentially the same as the Rainbow agent, with different hyperparameters to perform well when data is scarce [5].

5) I would argue that choosing the right hyperparameters for the algorithms that learn the state-action value distribution (the ones introduced in the paper) will significantly affect their performance on Atari100k.

6) Why has the entire Atari100k suite been plotted? The Atari100k benchmark is composed of 26 games, but there are only 24 plots in Figure 1 (supplementary PDF). What is happening with the other games?

7) Figure 2 gives the impression that Dueling is always effective across all the games, but this is not true, as shown in Figure 1 (supplementary PDF). I suggest reporting the IQM metrics for all the games and including the learning curves as you are doing.

8) I do not see any positive benefits of Dueling in 10 games. Why is that?

9) It is difficult to draw conclusions from Table 3. The sample-efficient algorithms are missing. What if you tweak the hyperparameters for the other algorithms (C51/QRDQN/IQN)?

10) How do you define the learning rate and epsilon for the agent? I do not see this information in Table 1 (supplementary PDF).

### Questions
**Please read the comments and questions in the weaknesses section.**

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper provides a fundamental perspective, questioning the methodological and design choices of deep RL algorithms. It specifically focuses on value based deep RL algorithms and addresses questions around sample complexity and monotonic improvement of deep RL algorithms, in both the low data and high data regime. For experimental ablations, it uses the ALE benchmark, and presents new findings showing that an algorithm performance can vary in different regions of sample complexity; and claims that recent works may have been built from incorrect conclusions, since they implicitly assume that algorithm performance in asymptotic regime is a clear indicative that the same algorithm would also outperform in the low data regime. Finally, through careful empirical experiments, with supporting theoretical statements, this paper shows that some of the baseline Q algorithms from few years back, can still outperform model value based deep RL algorithms which claim to be state of the art.

### Strengths
In my opinion, this paper’s biggest strength is how carefully it chose to analyse some existing algorithms, and addresses really fundamental questions that provides new perspectives to commonly held beliefs. It is a well written paper with findings presented clearly; with supporting theoretical statements drawn from prior works. It is works like these that encourages other researchers in the community to often revisit fundamentals, even when the community is moving towards a different direction scaling up existing algorithms. Without such works, often common misconceptions will have a long lasting effect, incorrectly misleading recent works, while issues existing in fundamental algorithmic principles. 

I would like to point out few key strengths of the paper : 

1. The findings are presented carefully and the paper is well written (although can sound a bit repetitive in certain cases). Given the vast majority of value based or policy based algorithms, it is often hard to pick existing algorithms to do careful ablation study. As such, the authors pick value based RL algorithms, specifically Q algorithms from the starting of the deep RL era, and compares to recent algorithms that are claiming to be state of the art. 

2. Past works have studied reproducibility or reliability issues in deep RL (Henderson et al., 2017) or even questioned about empirical reporting metrics often used for analysing performance of deep RL algorithms (Agarwal et al., 2021). While these works have raised issues around deep RL algorithms, often leading to the community being more aware of such issues - this work takes a different route compared to those and addresses a fundamental question : around sample complexity of deep RL algorithms, and what conclusions does the community draw looking at the asymptotic performance regime of modern RL algorithms. 

3. It is easy to believe that when a deep RL algorithm performs well in high data or asymptotic regime, other works tend to build up from it quite easily, with the race towards state of the art. In value based deep RL algorithms, several works often compare to the 100k ALE benchmark, or the 200M training frames ALE benchmark - and only compares to existing baselines that seem promising in these benchmarks. The issue arises when these new algorithms are built from other fundamental Q algorithms, and since they already claim to outperform those prior baselines in the ALE benchmark - any new work would tend to ignore the prior baselines and only compare to the recent ones. This becomes exacerbated when performance is only compared to a particular sample complexity regime - often comparing asymptotic performance. 
This work does a great job in pointing out that algorithm performance may vary depending on different sample complexity regimes. While past works may have implicitly been aware of this, e.g when analysing differences in performance curves - this was never formally studied through the lens of theoretical sample complexity and empirical performance. The findings in this work are clear and presents interesting insights. 

4. Experimental results are well presented, and the figures provide clear insights on the different range of modern to older deep RL algorithms. One quick suggestion here for improvement would be to make the figure captions more self explanatory - ie, to include the conclusion/insight drawn from each result in the caption itself, without having to refer to the figure and look into the paper text for the conclusion drawn from that particular figure.

### Weaknesses
 While the paper provides interesting insights and carefully presents findings and conclusions, there are few things maybe worth highlighting here. 

1. Some of the text and findings in the paper often seem repetitive; maybe worth re-writing few parts of it. 

2. I think the issue raised here are fundamental around deep Q algorithms, and not specifically to any distributional Q learning algorithms. Often the reference to distributional RL in the text seem confusing and presented as if the conclusions are only when comparing sample complexity regime for distributional Q algorithms. If I understand correctly, the paper presents the issues that are more generic to distributional RL - so it might be worth clearly stating that and not convoluting too much with distributional Q algorithms here. Please correct me if I’m wrong here. 

3. Experimental comparisons are often made between Dueling, IQN, C51 and others - referring to the comment in (2), if we do not present results specifically to distributional Q algorithms, would it be possible to also present basic Q algorithms (like DQN for example, or some variant of DQN) in the figures here? This would help put the paper in more context to addressing how the common misconceptions around performance and sample complexity exists widely - and that very basic deep Q algorithms may in fact still be good depending on the sample complexity regime being analysed. 

4. I think (also referring to Q3 below) - the bar for this paper can be increased significantly if some policy based algorithms are also introduced in the experiments for a comparison. 

5. (Minor) : Figure 4 can be hard to understand and not clear what exact message it is trying to convey. It might be useful to make the caption more self explanatory.

### Questions
1. I do not intend to add a question here that raises the experimental requirement significantly; but if it is within the scope of the work - maybe one or two experimental results also introducing policy based algorithms in this context might make the paper really interesting. For example, if you pick basic PPO or TRPO for these ALE benchmarks - can we see how those algorithms also compare to these existing ones, in different sample complexity regimes?

2. Maybe outside the scope of the paper - but this issue around performance comparison in different sample complexity regime also exists between deep policy based and value based algorithms. Can the authors provide some results showing comparisons between value and policy based algorithms here?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Authors claim that conclusions of deep rl algorithms comparisons only hold for the data regime the algorithms were trained on. Hence, they compare distributional and classical deep q-learning on both the atari 100K and the atari 200M benchmarks. They infer that unlike what has been claimed by recent research performed in the low data regime (DRQ, Simple, ...) Dueling Q-Learning (Wang 2016) appear to be the regime-independent SOTA.

### Strengths
The main claim of the paper that conclusions about deep rl only holds for the data regime they are trained on is very smart and properly supported in the paper. Lots of experiments were conducted. This paper's claims are of great importance for the rl community.

### Weaknesses
I find this paper poorly written and poorly presented.

For me, the main weakness of the paper is that the main claim of the paper is so well supported by fig 1 (which is by the way repeated in fig 4) that adding all those proofs and learning curves in the main paper just kills its readibility and target audience which should be the whole RL community.
 
I think the proofs should go in the appendix and the experimental section needs to be rewritten.

In particular, baselines and environment could be described in distinct paragraphs which would prevent having so much acronyms. For example, why define DRQ^ICLR instead of just citing a paper ? 

To rewrite the experimental section, you should have a look at the omitted empirical rl litterature. You can find some papers there : https://esraasaleh.com/cs-blog/experimental-rigour-in-machine-learning/ . I would particularly recommend the author to look at:
- Deep Reinforcement Learning at the Edge of the Statistical Precipice 2021
- Empirical Design in Reinforcement Learning 2023
- AdaStop: adaptive statistical testing for sound comparisons of Deep RL agents 2024

In particular, you can reproduce fig 5 of AdaStop: adaptive statistical testing for sound comparisons of Deep RL agents 2024 or fig 9 of Deep Reinforcement Learning at the Edge of the Statistical Precipice 2021 with some atari games in both the low and high data regimes.

### Questions
- Cite Arcade Learning Environment line 37.
- What does canonical mean in your introduction?
- Is it really true that people make the assumption of monotonic data regime (lines 40-46)? Maybe you should add citations.
- Missing citations for MDPs QRDQN, IQN, ... in the preliminary section.
- Can you confirm that your Human normalised scores are obtained by evaluating the learned policies (the Q-nets) outside of the training loops ?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors argue that the performance of RL algorithms in the high-data setting may not be indicative of the performance in the low-data setting. In particular, they emphasize the difference of distributional RL in the low and high data settings. They demonstrate this with experiments in the Atari 100k setting and theoretical results based on the linear function approximation setting.

### Strengths
I think that questioning our experimental settings is always a valuable contribution, and it’s nice to see more concrete evidence that the Atari 100k benchmark doesn’t necessarily generalize to the general Atari benchmark.

### Weaknesses
Clarity: The writing is extremely superfluous in many places and this makes it hard to follow the contributions and the arguments being made.

Overclaims:
- One claim in the paper is that the distributional RL may harm early learning, however, comparing C51 to Dueling is not a direct comparison, since it introduces a new technique. A fairer comparison would be C51 + Dueling to Dueling or C51 to DQN.
- I’m not sure I agree that the experiments are “large scale extensive” as the results omit several notable modern algorithms for Atari 100k (e.g., BBF, EfficientZero, DreamerV3) and only examine a single setting.
- Line 507 states “Our paper demonstrates that several baseline Q algorithms perform better than a line of recent algorithms claimed to be the state-of-the-art” but the results only show that Dueling DQN outperforms some other DQN-based algorithms designed for the full Atari setting, in the Atari 100k setting. But it doesn’t show Dueling outperforms actual SOTA algorithms for Atari 100k, nor does it show Dueling outperforms algorithms in the full Atari setting, so I’m not convinced by this claim.



### Questions
- It’s unclear to me what the incorrect conclusions made by prior work are exactly, could you expand on this point? (line 83) 
- In Figure 1, shouldn’t dueling be attached to several of these methods, such as Rainbow, OTR, DER, and DrQ, which all use the dueling architecture? 
- How much data is the high data regime results in Figure 1 (right) based on? Since these results don’t seem to correspond to the original paper results. 
- Line 416 talks about the performance of DRQ vs Dueling, where are these numbers coming from? (Table or figure?)

### Soundness
1

### Presentation
2

### Contribution
3
