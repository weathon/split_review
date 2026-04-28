# PFGuard: A Generative Framework with Privacy and Fairness Safeguards

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 8, 6, 3, 8

## Abstract
Generative models must ensure both privacy and fairness for Trustworthy AI. While these goals have been pursued separately, recent studies propose to combine existing privacy and fairness techniques to achieve both goals. However, na\"ively combining these techniques can be insufficient due to privacy-fairness conflicts, where a sample in a minority group may be amplified for fairness, only to be suppressed for privacy. We demonstrate how these conflicts lead to adverse effects, such as privacy violations and unexpected fairness-utility tradeoffs. To mitigate these risks, we propose \ours{}, a generative framework with privacy and fairness safeguards, which simultaneously addresses privacy, fairness, and utility. By using an ensemble of multiple teacher models, \ours{} balances privacy-fairness conflicts between fair and private training stages and achieves high utility based on ensemble learning. Extensive experiments show that \ours{} successfully generates synthetic data on high-dimensional data while providing both fairness convergence and strict DP guarantees -- the first of its kind to our knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents PFGuard, a framework for jointly private and fair generative models. The challenges of naively integrating an unfairness mitigation scheme within private generative models are considered. The paper presents an algorithm based on importance sampling to mitigate unfairness first and then privatize using a teacher ensemble a la PATE.

### Strengths
- The idea of controlling the fairness-privacy tradeoffs for generative application is worthwhile.

- The writing is clear and easy to follow.

### Weaknesses
 - **Algorithm likely has unaccounted-for privacy leakage.** The paper claims that the privacy of Private Teacher Ensembles comes from data disjointness alone.  This is not true; that guarantee also depends on random partitioning of the private data; therefore not only disjointness is required but so is random sampling. The importance sampling step that the paper employs cannot, by definition, be completely random as it has to take into account sensitive group. This means that there is an additional privacy cost to this sampling step that the paper simply does not consider. Using importance sampling in DP settings for fairness is not new. In fact, one of aforementioned papers Kulynych et al. 2021 do this while also accounting for the privacy cost of importance sampling.

- **Claims of novelty are exaggerated.** The contribution of the paper is doing private and fair generation; its claim novelty is generation as classification has been done before; yet the private generation is achieved via other methods. In general, reading through Section 4 and especially Section 4.3, the paper is lacking substance regarding the particularities that introducing fairness to private generation brings. Over-relying on prior work like (Jordon et al., 2018; Chen et al., 2020; Long et al., 2021; Wang et al., 2021a) has left the analysis incomplete and without justification. 
  
  For instance, I believe this statement on  Line 315 is wrong:  
  
  > PFGuard preserves any sensitivity as long as the PTEL enforce data disjointness; even with fair sampling, a single data point still affects only one teacher.  
  
	- How come? Can't a point in the minority group be resampled to maintain a similar data distribution across all teachers as assumption (2) (Line 256) requires? Speaking of Assumption 2:

- **Assumption (2)-Line 256 is unrealistic.** paragraph on Line 254 reads:
  > Methodology We now present our sampling technique, which guarantees $B \sim p_{\text {bal }}$ based on SIR. We first make the following reasonable assumptions: 1) each data sample has a uniquely defined sensitive attribute $s \in S$ (e.g., race); 2) $p_{\text {bal }}$ is uniformly distributed over $s ; 3$ ) following Choi et al. (2020), the same relevant input features are shared for each group $s$ between the balanced and biased datasets (e.g., $p_{\text {bal }}(\mathbf{x} \mid \mathbf{s}=s)=p_{\text {bias }}(\mathbf{x} \mid \mathbf{s}=s)$ ), and similarly between the training dataset $D$ and any subset $D_i\left(\right.$ e.g., $\left.p_D(\mathbf{x} \mid \mathbf{s}=s)=p_{D_i}(\mathbf{x} \mid \mathbf{s}=s)\right)$ . We now outline the technique step-by-step below.  
  
	- Assumption 2 here means that samples can be balanced out in terms of sensitive group membership. This assumption is unrealistic. How can the sensitive feature be uniformly distributed; when by definition there exists minority and majority sensitive groups? The only possible way I can think of that would make this work in any practical setting is by resampling minority samples over and over. But that is bound to increase the privacy cost.

- **The paper is missing a number of relevant prior work.** I have already mentioned Kulynych et al. 2021  which essentially does importance sampling for DP-SGD. Also, state-of-the-art for private and fair classification is DP-FERMI by Lowy et al. 2023 is not really considered. Remark 1 on page 4, regarding being the first to revleal that fairness and privacy tecnhiques can counteract each other is not true. Yaghini et al. 2023 and Tran et al 2021  and other make the same observations under PATE classification. I am well-aware of the authors contention in Remark 2 and Section A. So I am going to provide counter-arguments why I cannot accept their line of arguments there in.

	- First, authors claim the other works Jagielski et al. 2019 Mozannar et al. 2020 Tran et al 2021 Lowy et al. 2023 all use DP w.r.t. sensitive attribute hence they account for a different DP definition. While that is true of the first 3, it is not true of Lowy et al. 2023, neither is it true for Kulynych et al. 2021 or Yaghini et al. 2023 who all consider central (i.e. w.r.t all attributes) DP as well. Incidentally, Tran et al 2021 and Yaghini et al. 2023 setting is over PATE which is pretty close to the PTEL setting of the paper modulu the generation part. But as established earlier, the present paper does not advance the generative setting beyond prior work.

	- Second, it is unclear to me why challenges of accounting for the privacy cost of adjusting C plays any role in those works not being considered as baselines. If these methods budget their privacy allocation poorly, doesn't that make for a stark and interesting comparison? To be honest, I do not believe these are the best baselines to compare against but I found this line of argumentation faulty.

### Questions
- Can you justify assumption 2 on Line 256? (see my feedback in the weaknesses part)

- Can you include one of the aforementioned baselines?

- Do you acknolwedge the additional privacy cost of importance sampling? Can you address that in a meaningful way?

- Have I misunderstood part of your work? To be clear, I think as is, this paper is not ready for publication. However, I want to be fair and make sure that I have not misunderstood your work. So I'll be happy to engage with you during the rebuttal process.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies tensions between fairness and privacy in generative models. It proposes PFGuards, a framework leveraging an ensemble of teacher models to jointly enforce fairness and differential privacy while preserving utility. The proposed method consists of training an ensemble of fair teachers using balanced minibatch sampling and using their differentially private (leveraging the PATE framework) aggregated output to train a privatized generator. Experiments demonstrate improved performances in fairness and utility compared to existing approaches.

### Strengths
- Good quality of the presentation
- Extensive experiments on MNIST, FashionMNIST, and CelebA
- Comparison against several baselines, including fair variants of DP-SGD

### Weaknesses
 - Limited choice in epsilon values, making it difficult to understand the effect of privacy budget on utility and fairness
- The choice of datasets and bias settings makes it difficult to determine whether the method would perform effectively in real-world scenarios. I recommend incorporating tabular datasets, as done in (Tran et al., 2021b), to assess group fairness. Additionally, it would be valuable to explore alternative fairness notions for datasets where group fairness may not be applicable

### Questions
- Is there any consistent trend in utility and fairness as the privacy budget increases? I would suggest the authors to perform a similar analysis as in (Tran et al., 2021b -- Fig. 2)
- Given the high-dimensional context, other fairness notions, such as Rawlsian Max-Min fairness, could be more appropriate. Can the framework proposed extend to such notions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on data privacy and model fairness for developing generative models. They claim natively combining differential privacy and fairness learning techniques may cause conflicts, and then propose PFGuard framework to simultaneously balance the two objective and also the utility. The core insight is to employ an ensemble of multiple teacher models. And they also do experiments on GANs with images datasets as benchmarks to show a better trade-off can be achieved.

### Strengths
1. I agree with the authors that the conflicts between data privacy and fairness do exist for generative models. It is an interesting research problem to be explored by research community.
2. I think importance resampling can be a useful approach to get balanced training data, which is helpful to train a fair generative model.
3. The experiments shown in tables demonstrated that better utility and fairness are achieved by fixing a privacy budget.

### Weaknesses
1. The authors have claimed the interested privacy of this paper is to defend against training data reconstruction, while naive differential privacy techniques preserve the membership instead of data content. This has been recognised in the early work [1] but ignored by this paper.
2. Since only a smaller training data is derived after resampling for fairness, this may degrade the quality of generated data, as claimed in [2]. In this case, the quality of generated data will be sacrificed.
3. It is easy to understand that minority samples should be upweighted in fairness. But in what scenarios minority samples should be downweighted for DP? Because sensitivity controls the strength of the added noise, maybe how will minority samples affect the sensitivity should be explained.
4. In Fig. 3, reweighted and rewerighting are both used.  Are they same? In addition, it seems privacy budget is fixed and then the trade-off between utility and fairness is studied, and so as to experiments. This is not aligned with the motivation where fairness and privacy conflicts.
5. The proposed framework is a sequential procedure where the first component is about fairness while the second one is for privacy. In this sense, it is not very convincing to say they two can be better traded off.
6. I would like to see some Pareto front results in terms of three metrics, which can better demonstrate the proposed method.

### Questions
Please refer to Weaknesses.

Also, can you justify the novelty of using PTEL in this work? Because this is the main technique of the proposed framework.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces PFGuard, a framework for privacy-preserving generative models that integrates fairness through a simple modification in the minibatch sampling process, specifically employing importance sampling based on group membership. The framework builds on PATE/PTEL, which is commonly used for privacy deep private generative models. The paper summarizes challenges in balancing privacy, utility, and fairness in generative models, then proposes the PFGuard framework (which relies on protected group-wise importance sampling), before finally empirically arguing that PFGuard achieves an improved balance of privacy and fairness.

### Strengths
This work quite successfully communicates the challenges in achieving the privacy/fairness tradeoff. I particularly appreciate the clarity of Figures 1, 2 and 3, along with the care with which the experimental results in Tables 3 and 4 are presented. Additionally, I believe that this is an interesting problem that deserves attention. I have closely read the main paper body, and appreciate the lack of obvious grammatical errors - overall the paper is well written.

### Weaknesses
Unfortunately, though the paper writing and presentation is of high quality and clarity, there are issues in terms of originality, significance and correctness.

W1: I’d like to highlight that Remark 1 (on novelty) is not correct and should be removed or further qualified. There appears to be ample prior work that “reveals how fairness and privacy techniques can counteract each other,” some in a more formal ways than this work (Bullwinkel et. al, https://arxiv.org/pdf/2205.04321 , Rosenblatt et. al https://arxiv.org/pdf/2312.11712 , Abroshan et. al (https://proceedings.mlr.press/v238/abroshan24a/abroshan24a.pdf , Cheng et. al https://dl.acm.org/doi/pdf/10.1145/3442188.3445879 )

W2: Additionally, Remark 2 either needs to be removed or needs further clarification - why would we extend classification techniques to the generative setting? Differentially private data generation (both synthetic tabular, see Mckenna et al 2019, 2024, https://proceedings.mlr.press/v97/mckenna19a/mckenna19a.pdf , https://arxiv.org/pdf/2201.12677 , Liu et. al 2021, 2023 https://proceedings.neurips.cc/paper_files/paper/2021/file/0678c572b0d5597d2d4a6b5bd135754c-Paper.pdf , https://proceedings.mlr.press/v202/liu23ag/liu23ag.pdf AND image Ghalebikesabi  et. al https://arxiv.org/pdf/2302.13861 ) is a very mature field, under much lighter assumptions then are necessary for PATE/PTEL.

W3: (W2) leads me to my main issue with the empirical results, which is that this is a bit of an apples to oranges comparison (or at least, it's not obvious that the comparison issue I see has been properly addressed). As you acknowledge, and as is the standard assumption with the PATE framework, we assume access to “ a public reference data on the order of 10%–100% of |D| for the estimation” (line 281). However, some comparisons in your paper (for example, in table 3) compare PFGuard directly to a method like DP-SGD (with further modifications), and for which it is not clear if the public reference data assumption is leveraged by the DP-SGD fit model (there are existing methods to help do this). 

In fact, assuming an unbiased public reference sample is quite a strong assumption, and having no experiments on how a biased public reference sample would effect your results is questionable. Additionally, if I had access to a public reference sample, even only 10% of some large data sample |D|, why wouldn’t I just train on this sample? I’m missing where you note something about label missingness in this public sample, but maybe that isn’t the assumption? Is the assumption that we have full access to this public unbiased sample, and that its size is substantial? We would certainly want to compare to just training on that if this were the case.

W4: My 1 sentence summary of the proposed methodology here is as follows: take the PATE/PTEL framework, and during the sampling for teacher creation, use importance sampling based on group membership. This, in of itself, is a reasonable approach, but it is not clear to me how this work improves on the component parts of the PFGuard method (which are well established and well studied methods), besides using them in tandem. Nor does that work consider the model of importance sampling and how that might affect utility in other ways from a formal perspective, despite considerable prior work on the utility of PATE (Bassily et. al, https://arxiv.org/pdf/1803.05101 ). Nor does it contend formally with any potential privacy concerns (even to just dispel this concern with a short proof or proof adjustment). Given that I have some issues with the assumptions of the empirical results, this leads me to my score.

### Questions
All that said, I am open to raising my score slightly if the authors can adequately address the following questions,

Q1: How precisely is the public reference sample handled experimentally? Are all methods given “equal access” so to speak? If the sample is assumed to be complete (i.e. containing all relevant columns from D) also please provide a test on the same metrics you present for the private/fair methods of simply using the holdout sample at different subsample percentages on each task.

Q2: Why should we use importance sampling, instead of just constructing (potentially deterministically) balanced samples using stratified sampling? It seems believable (although is not proved here) that in the PATE/PTEL framework we can use whichever sampling technique we want, so long as it is randomized (although this is not explicitly proven by the authors or cited). However, given that, AND the assumption of access to the membership of samples in protected classes, importance sampling vs. stratified sampling should be explored. Or maybe I’m missing something.

Q3: Please, if you can, offer a more formal characterization of how importance sampling does not effect the privacy guarantee of PATE/PTEL. You can also use the framework presented in Bassily et. al .

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this work, the authors study the intersections of fairness and privacy in generative models, and show that these two goals can come into conflict. Furthermore, they highlight that naively combining existing fairness and privacy methods can fail. They propose PFGuard, a framework for achieving fairness and privacy simultaneously and then conduct experiments validating their method.

Overall, I think this is a paper with great contributions and analysis. I think some of the boldest claims should be softened, but otherwise I think it is a good candidate for ICLR.

### Strengths
Strengths:
 * I really liked the discussion of how fairness and privacy can come into conflict. I think it is somewhat "folklore" in the trustworthy ML community so I appreciated a more detailed discussion of the topic, especially in Section 3.
 * The PFGuard framework is a great solution to the problem. "Isolating" the fair training component and then distilling this knowledge privately is a great approach that I could see being taken to do many different downstream applications that also require privacy!
 * I think it is good the authors acknowledge that fairness adjusts sensitivity, which can still be made private with more noise, but point out the amount of noise to add may be unclear or performance degrading.

### Weaknesses
Weaknesses:
 * The authors focus on GANs as opposed to Diffusion Models, lessening the contemporary impact of the paper. This isn't necessarily a weakness, more an observation.
 * In Section 3, you start with **Adding Fairness Can Worsen Privacy** and describe in text some vague settings where fairness and privacy can come into conflict. I really wanted to see an elaboration or concrete example of how this could happen. I was very excited to see this in **Adding Privacy Can Worsen the Fairness-Utility Tradeoff** part! I think this is a great contribution. However, I think in the second part, you actually discuss both how fairness can worsen privacy (how fairness can modify the sensitivity, C) and then how adding privacy can worsen fairness (clipping worsens fairness adjustments). You should split these up according to the headers you wrote by moving the first example up to the first section. I would rewrite these two sections and cut some of the vaguer writing in the first section, and spend some more time elaborating on these two examples as they are a great contribution that I would be interested in more discussion of.
 * You say in Remark 1 that your study is the first to reveal that fairness and privacy techniques can counteract each other. I think this is too bold of a claim, given works you cite such as [1] and [2] that explore the topic.
 * I wouldn't say giving each teacher *probabilistically* one sample of the minority group is enough data to expect the teacher to be adequately fair. How did you come to this heuristic, and how can you justify it?
 * There are no fairness guarantees offered by this method because of data resampling and teacher distillation. I think the link between having balanced minibatches and the fairness of the teachers is more clear, but I wonder how distillation affects bias or if there is any literature you could cite here.

Notation:
 * Definition 2.1 - I would explain that domain $\mathcal{D}$ is a dataset, thus why D, D' can differ by a single sample.
 * You should also describe what function we measure sensitivity over. Is it the loss? is it the gradient? is it the model outputs? This will make it much clearer how exactly fairness interventions impact sensitivity in Section 3.

### Questions
Questions:
 * "Additional fair sampling does not require additional training complexity compared to say adding a loss term for fairness": I would argue that adding a loss term that can be backpropagated over is much simpler than having to do your complex sampling procedure to construct balanced minibatches. Can you justify or elaborate on why fair sampling is less complex? I don't think this claim is core to your paper so I think you could also do without it. You mention it later in the paper as well.
 * In your extensions to unavailable sensitive attributes, why do you need to train your classifier on less data? Given one of the benefits of PFGuard is any methods you apply before the teacher-distillation step need not be private, I would expect the best thing to do from a fairness perspective is train the best, beefiest sensitive-attribute classifier possible for fair training.
 * In your figures, why do you apply [method + PFGuard]? Isn't PFGuard an end-to-end fairness + privacy method? From what I can tell in your results you are applying PFGuard to existing DP generative models. This makes it difficult for me to interpret your results, and the unique impact of PFGuard on your results.
 * My intuition tells me that privacy always comes at a cost to utility, and this teacher + distillation procedure should be even more noisy than traditional DP-SGD methods. Can you comment on why this is not the case in your results? Why isn't a more advanced privacy method that permits fairness also resulting in further costs to utility than a traditional fairness method? How much of a fairness drop (from teacher fairness to generator fairness) do we incur because of the private distillation?

### Soundness
4

### Presentation
3

### Contribution
4
