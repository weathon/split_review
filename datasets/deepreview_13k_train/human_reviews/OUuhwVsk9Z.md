# Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel

- Decision: Accept
- Scores: 5, 5, 8, 8

## Abstract
Creating high-quality data for training robust language-instructed agents is a long-lasting challenge in embodied AI. In this paper, we introduce a Self-Refining Data Flywheel (SRDF) that generates high-quality and large-scale navigational instruction-trajectory pairs by iteratively refining the data pool through the collaboration between two models, the instruction generator and the navigator, without any human-in-the-loop annotation. Specifically, SRDF starts with using a base generator to create an initial data pool for training a base navigator, followed by applying the trained strong navigator to filter the data pool. This leads to higher-fidelity data to train a better generator, which can, in turn, produce higher-quality data for training the next-round navigator. Such a flywheel establishes a data self-refining process, yielding a continuously improved and highly effective dataset for large-scale language-guided navigation learning. Our experiments demonstrate that after several flywheel rounds, the navigator elevates the performance boundary from 70% to 78% SPL on the classic R2R test set, surpassing human performance (76%) for the first time. Meanwhile, this process results in a superior instruction generator, as reflected by the improved SPICE from 23.5 to 25.7, better than all published approaches tailored for VLN instruction generation. Finally, we demonstrate the scalability of our method through increasing environment and instruction diversity, and the generalization ability of our pre-trained navigator across various downstream navigation tasks, surpassing state-of-the-art performance by a large margin in all cases. Code is uploaded as supplementary materials and all our data/code/models will also be publicly released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces the Self-Refining Data Flywheel pipeline within the context of Vision-and-Language Navigation (VLN). This pipeline iteratively improves itself by generating navigation instructions and refining navigation paths through repeated cycles of self-improvement. The goal is to enhance VLN performance by creating a feedback loop that iteratively optimizes both instruction generation and navigation, facilitating autonomous performance improvements over time.

### Strengths
- Simplicity and Effectiveness: The concept of iteratively refining instructions and navigation steps is straightforward, yet the experimental results validate its utility in enhancing VLN task performance.

- Clarity and Structure: The paper is well-written and clear, with a structured presentation that helps readers understand the pipeline. Additionally, it effectively contextualizes the work within existing VLN research, making its contributions easy to follow.

- SoTA performance: While I'm not an expert in the fields of VLN, it seems the paper achieved the good performance compared to the prior SoTA>

### Weaknesses
 - Terminology and Scope: The term "Flywheel" might be overly strong for what is essentially a straightforward iterative self-improvement process, and it could be perceived as a bit exaggerated.

- Limited Dataset Scope: The method is only tested on the R2R as a base dataset, and the lack of the discussion on its broader applicability.

- Limited Analysis of Performance Boundaries: While performance improvements are reported in up to three rounds (Table 3), little discussion exists on why the improvement plateaus and whether there are theoretical or practical limits to the approach’s performance gains.

- Positioning within Broader Self-Improving Frameworks: The novelty of this approach needs to be clarified when considering related research beyond VLN. The "Self-Improving Language Models" section lacks a strong position on how this framework differentiates itself within the wider landscape of self-improving models.

### Questions
1. How does performance change when using a different baseline from R2R? Could the choice of base data impact the outcomes, and if so, how?

2. SPL and nDTW are used as metrics for improvement. Could you explain why these were chosen specifically, and how would the results differ with alternative metrics?

3. Considering research outside of VLN, what novel aspects of this framework make it distinct within the scope of self-improving models?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework in which the instruction model and navigation model bootstrap each other through an iterative process. It begins with the pre-trained instruction model labeling sampled trajectories, which are then used to fine-tune the navigator. The updated navigator subsequently samples additional trajectories to further refine the instruction model, and the cycle continues. The authors conduct experiments on various VLN benchmarks, including R2R, CVDN, REVERIE, SOON, R4R, and R2R-CE. The experiment results show that the proposed method is able to

### Strengths
1. The paper is well written and easy to follow.
2. The authors have conducted experiments on diverse downstream VLN tasks to validate the effectiveness of the method.

### Weaknesses
1. My major concern is the novelty of this paper. The proposed method highly resembles the Speaker Follower model (Fried et al., 2018), and the self-training paradigm has been widely studied in previous studies [1], [2]. 
2. It’s unclear whether the performance improvements primarily result from the bootstrapping process between the instruction model and navigation model, or from the advantage of initializing the instructor with a pre-trained MLLM (Mantis) that has been trained on a large-scale dataset. From Table 3 we can see that the model improves by a visible margin after round 1, but subsequent rounds yield only marginal gains. Prior studies [3] also indicate that generally, the self-training paradigm does not improve model's capabilities on out of distribution cases by much. It will be interesting to see how model's generalizability improved without relying on the pre-trained MLLM.
3. Some of the notations are not defined clearly. For example, what is D^N_1 and what is the data source of it? It is also unclear to me what is the exact dataset use to produce D_seed.
4. The author mentioned that they use DUET as the baseline navigator, could the author explain the performance discrepancy between the baseline in Table 3 (SR=78) and the DUET model in Table 7 (SR=72)?

In short, I think my major concern is the novelty of the paper. Also, I'm not sure whether the model is benefited by the powerful pre-trained MLLM or the bootstrapping process itself.

### Questions
1. Why is the performance of the speaker-follower model much lower than the results presented in the original paper?
2. Which dataset and split is used in the experiment reported in Table 3?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes an iterative instruction-generation and navigation pipeline to increase the quality of machine-labeled data for Vision Language Navigation tasks.  By using a navigation model to identify which generated instructions are achievable, the navigation model can improve the instruction generator's data.  This in turn creates a better instruction generator, which can expand the set of data used to train the navigation model.  The paper shows that by repeating this filtering/training cycle, the resulting navigator can perform comparably (or better than) humans on some benchmarks, and also that the instructions generated by the model are better than other baselines.

### Strengths
- The presented method generates impressive empirical results in the navigation task and in the instruction generation task as well.  The evaluations show the importance of carefully selecting (or generating) data to train VLN models.  Although this is not a new observation generally, the thorough and careful application of filtering and data labeling to the VLN problem is a solid contribution with state of the art results.
- Comparison to related work is thorough, both in evaluations and in the text.
- Presentation is clear and highlights strong results without grand claims.  The diagrams are helpful in understanding the approach.  Detailed description of implementation.

### Weaknesses
I found few substantial weaknesses in this paper.  Here are some minor suggestions:
- Radar plot in Fig 1. is difficult to read, the Human results are difficult to distinguish from ScaleVLN.
- Line 234 says "navigator $G_1$" which I believe should be $N_1$

### Questions
- The paper mentions several times that the navigator model being trained is already very good.  What happens in the case where the navigator is not as good?  Do you expect several more rounds of the flywheel to be required?
- Why does the paper stop at 3 rounds for evaluation?  I expect diminishing returns, but is that a reflection of the lack of high-quality data remaining for the model to label, or something else?
- When discussing label diversity, the paper mentions that the vocabulary size of existing datasets is small.  Can you say more about the effect of vocabulary size?  If, for example, the dataset were relabeled by asking a LLM to rephrase the instructions, would that be sufficient to get better performance?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a self-refining data flywheel (SRDF) approach to generate the high quality the instruction data for vision-language navigation task. It proposes a generator and navigator iteratively tuned to train each other. First, a navigator and a generator are trained on the base corpus, then the navigator serves as a filter for the generator to collect high-quality synthetic data, then refine the navigator with synthetic data iteratively. Empirical experiments on several standard vision-language navigation datasets (R2R, CVDN, R4R, REVERIE etc.) show very promising results.

### Strengths
1. An interesting paper to show that iteratively tuning the generator and navigator works in the vision-language navigation, and also demonstrates the state-of-the-art results on several tasks. The empirical results are impressive.

### Weaknesses
1. It looks this work (proposing iteratively tuning generator and navigator), is a upgraded version of Speaker-Follower model, which you can think it is only the first iteration of the model. Could you discuss in more details about the relevance and difference with Speaker-Follower in the paper?



### Questions
Some questions -

1. For the table 5, the number of instructions, did you use multiple instructions encoders (with one path trajectory) as input? for example, N=3, do you treat (3 instructions, one trajectory) as one instance? or (3 instructions, one trajectory) as three (1 instructions, one trajectory) instance? This is quite different.  If your input is multiple instruction encoders (or shared encoder for multiple instructions as input), this is quite different with one instruction input. 

Could you clarify the exact input and encoding process for this part?

2. And also for the main table 7, how many instructions per path trajectory in your setting?

3. Did you try this method on a different environment? rather than on R2R environments. Nearly all the tasks of this work are built on the R2R environments.  One question here is the generalization of the proposed method, if you could try out-of-domain environments, for example, ALFRED task?

### Soundness
3

### Presentation
3

### Contribution
3
