# CADO: Cost-Aware Diffusion Models for Combinatorial Optimization via RL Fine-tuning

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Recent advancements in Machine Learning (ML) have demonstrated significant potential in addressing Combinatorial Optimization (CO) problems through data-driven approaches. Heatmap-based methods, which generate solution heatmaps in a single step and employ an additional decoder to derive solutions for CO tasks, have shown promise due to their scalability for large-scale problems. Traditionally, these complex models are trained using imitation learning with optimal solutions, often leveraging diffusion models. However, our research has identified several limitations inherent in these imitation learning approaches within the context of CO tasks. To overcome these challenges, we propose a 2-phase training framework for diffusion models in CO, incorporating Reinforcement Learning (RL) fine-tuning. Our methodology integrates cost information and the post-process decoder into the training process, thereby enhancing the solver's capacity to generate effective solutions. We conducted extensive experiments on well-studied combinatorial optimization problems, specifically the Traveling Salesman Problem (TSP) and Maximal Independent Set (MIS), ranging from small-scale instances to large-scale scenarios. The results demonstrate the significant efficacy of our RL fine-tuning framework, surpassing previous state-of-the-art methods in performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new Cost-Aware Diffusion solver for combinatorial Optimization (CADO) method via RL finetuning. The existing approaches simply imitate the shape of the solution without considering the cost information. In addition, they do not account for the decoding process in the overall network. Lastly, they heavily rely on high-quality training datasets, which are expensive to collect. The proposed method trains a diffusion model with two phases: 1) SL and 2) RL fine-tuning. The proposed method incorporates the cost information and the decoder, which enhance the overall performance with significant efficacy.

### Strengths
- The existing three problems and motivations are well described.
- Experiments from small-scale to large-scale problems demonstrate the effectiveness of the proposed method.

### Weaknesses
 - Figure 1 shows the cost compared to the loss. However, the value difference is really small, which is not impressive.
- In two-phase training, the first phase is the same as DIFUSCO, and the second phase is just adoption of the existing decoder and RL algorithm. Overall, the method is really simple, and lacks a strong sense of novelty.
- The paper claims that the decoded solution may differ significantly, leading to degraded performance of the solver. Are there any example figures or quantitative results? From the main experimental tables, the performance quality is not significantly degraded, as the paper described.
- From the tables, the performance gap is minimal, making the results less impressive. In addition, it is uncertain whether the cost is significantly lower compared to other methods. In a certain dataset, the proposed method rather underperformed, showing inconsistent results.
- From table 4, it is unclear how sensitive the method is to dataset quality compared to existing algorithms. Moreover, this low-quality dataset setting does not look like a realistic setting.

### Questions
- Is the cost really problem? This task (CO) does not require a real-time solution, which means the cost gap between the proposed method and existing methods is not a significant problem.
- The proposed method trains the network with one more stage compared to the existing method. Is it a fair comparison? I wonder why the proposed method requires less time consumption compared to DIFUSCO. Moreover, as the experimental result shows, when DIFUSCO trains one more stage with the same SL, the performance is enhanced. It means the proposed method needs to be compared with other algorithms that run the same number of stages or iterations.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, a cost-aware diffusion solver CADO for combinatorial optimization is proposed, and a fine-tuning framework based on reinforcement learning is proposed for diffusion models in combinatorial optimization. CADO consists of two phases: in the first phase, the diffusion model is trained using a given data set, and in the second phase, the pre-trained diffusion model is fine-tuned using reinforcement learning. Finally, it is applied to the traveling salesman and the maximal independent set problem.

### Strengths
1.The experiments are relatively full and complete, comparing multiple methods, and doing a wealth of experiments on different datasets for different problems.
2.Good results were obtained on different datasets.
3.To the best of our knowledge, current techniques using diffusion models as well as RL fine-tuning are not common in combinatorial optimization. This paper  provides a detailed code open source for the implementation of the algorithm, which provides a baseline for subsequent similar studies.

### Weaknesses
1.The innovation of the method is relatively low. The method of training and fine-tuning is very simple, which is slightly lacking as the innovation point of this paper. We do not see the authors' approach as a significant change from existing algorithms based on reinforcement learning fine-tuning.
2.The motivation also lists some basic problems in the field of combination optimization. It is not seen that these problems are essentially solved, especially (3.2) and (3.3). Alternatively, the authors do not do a good job of explaining why their approach is necessary to solve these difficult problems. In addition, (3.1) has always been a difficult problem faced by the traveling salesman problem, and there is no obvious groundbreaking. 
3.Overall, after reading the entire article I'm still not sure why the algorithm in the article works. Why they achieved better results compared to other algorithms and why this framework is necessary for combinatorial optimization.

### Questions
We will consider revising the evaluation based on the answers to the following questions.
1.Please highlight the core contribution points of the article. The method of supervised learning and fine-tuning is more like a trick than sufficient to support the innovation of the article.
2.Specific method support for motivation. Taking feasible punishment and optimization goal as reinforcement learning reward is a very simple idea in the field of combinatorial optimization. Can this paper give more detailed and specific support for motivation.
3.We would like the authors to better explain why the framework in this paper is useful for the hard cases in combinatorial optimization. And what necessary adjustments the authors have made to the original reinforcement learning approach to ensure its applicability to combinatorial optimization problems. We recognize the validity of the experimental results in the article. But we also believe that a clear statement of the principles that make the algorithm effective is also necessary, especially for problems such as combinatorial optimization.

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
3

### Summary
This paper introduces RL finetuning to diffusion model-based combinatorial optimization solvers. The methodology seems to be built based on DIFUSCO and T2T, whereby a pretrained DIFUSCO is taken and fine-tuned with RL; and the decoding strategy in T2T is also considered. The main motivation and expected improvement is a CO solver should not only focus on mimicking the supervision signal but also consider the objective function to be minimized. Experiments on TSP and MIS show a little bit of marginal but solid improvements over state-of-the-arts.

### Strengths
* I found it interesting to involve objective function minimization in the training process. Introducing RL in training diffusion models for CO is a novel idea. 
* The improvement over baselines such as T2T and DIFUSCO is solid among the benchmarks considered in this paper.

### Weaknesses
 * The presentation does not discuss important peer methods properly, especially T2T. This paper is motivated by the fact that DIFUSCO does not consider the objective function and claims its contribution of involving the objective function by reinforcement learning. However, T2T has achieved consistent improvement over DIFUSCO by denoising with the guidance of the objective function (as one can tell from Tables 1,2,3), which the authors fully overlook. I understand the fact that this paper uses a different methodology (reinforcement learning), but T2T should be the most important peer method and the authors should not simply overlook that. Simply mentioning the following in related work is not enough
> (T2T and Sanokowski et al. (2024)) are similar to our work in that they utilized cost information, but those methods require a differentiable cost function
* Given the fact that 1) T2T is under a quite similar motivation, 2) T2T seems very competitive, the experimental improvement over T2T is less significant than the improvement over DIFUSCO, 3) the guided denoising strategy in T2T seems to be used in CADO (this paper)
> L304: We also enhance our method with an optional local search technique inspired by Chen & Tian (2019) and Li et al. (2023) called local rewriting. This involves strategically reintroducing noise followed by a secondary denoising process, allowing us to explore the solution space beyond initial denoising results

    I believe there needs more discussions and ablation studies on the introduced RL methodology: when comparing RL-finetuning (this paper) solely with guided denoising (T2T), which contributes more to the objective score? What is the understanding of faster inference on TSP but slower on MIS? The local rewriting technique, while inspired by T2T, needs more clarification on whether it uses the cost gradient guidance during the secondary denoising process, as in T2T, or if it is a simplified version. The performance differences between CADO and T2T are not well-understood, especially given the similarities in their approach to incorporating cost information.
* Another important point this paper failed to address is its technical contribution: introducing RL to optimize the objective score is straightforward (there are tons of RL for CO related work on this), and fusing RL with diffusion is performed by following Black et al. (2024). What is the technical challenge resolved for the combination of RL, diffusion, and CO? The paper needs to articulate the specific challenges in adapting RL to diffusion-based CO solvers, especially given the high-dimensional action space of heatmap solvers, and how the proposed method addresses these challenges beyond simply applying existing techniques. The novelty of the approach needs to be more clearly defined, highlighting the unique aspects of the proposed method compared to existing RL for CO methods.

Typo/misc
* "Figure 5" is a table
* Citation for T2T in the upper half of Table 1 is wrong.

### Questions
I like the general idea of introducing RL to DIFUSCO and the solid improvement on TSP (better objective score and inference time) and improvement of objective score on MIS (slower inference, though). Before being fully convinced to suggest an acceptance for this paper, I would love to see more discussions on related work (especially T2T, which is missing in the current manuscript), and more insights among different ways of integrating the objective function into CO-solving.

I would like to suggest the following improvements in future versions & in the rebuttal:
* A dedicated subsection comparing CADO with T2T, focusing on these different approaches to incorporating cost information and their relative performance across various problem sizes and types.
* An ablation study that isolates the effects of RL fine-tuning and guided denoising. Additionally, A detailed analysis of the performance differences between TSP and MIS tasks will be nice, particularly focusing on the trade-offs between solution quality and inference time.
* A subsection to explicitly outline the novel technical challenges they encountered in combining RL, diffusion models, and CO. It will be nice to detail how your approach differs from simply applying existing techniques, and to highlight any innovations in your methodology that address CO-specific challenges.

One more technical question:
* This method is faster than T2T and DIFUSCO in Table 2. What is the methodology that made it possible? Why does it get slower than T2T and DIFUSCO in Table 3?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes CADO, a novel Cost-Aware Diffusion solver for combinatorial optimization (CO) tasks that address key limitations in traditional heatmap-based solvers, which typically rely on supervised learning to imitate optimal solutions but neglect cost information and the decoding process. By introducing a reinforcement learning (RL) fine-tuning phase, CADO integrates these elements directly into the training process, improving solution quality and computational efficiency. Applied to CO problems like the Traveling Salesman Problem (TSP) and Maximum Independent Set (MIS), CADO demonstrates superior performance, reducing computational costs by 15-40% and outperforming state-of-the-art solvers across various benchmarks.

### Strengths
1. This paper presents an interesting point that lower prediction errors do not always correlate with better solution quality. The introduction of an additional RL fine-tuning process is well-motivated to address the shortcomings of existing SL frameworks.

2. This paper introduces a novel two-phase training framework that combines SL with RL fine-tuning, addressing key limitations of traditional heatmap-based CO solvers.

3. The method design is reasonable, and the experimental results are convincing.

### Weaknesses
1. Cost guidance for models through post-training optimization has been explored in previous works, such as gradient search and local search [1,2]. The authors should address the differences between their approach and these methods, and discuss any potential advantages their method offers.

2. The methodology design appears somewhat simplistic, as it essentially applies RL on top of diffusion models. Yet, the strength of the paper, which includes motivation, discussion, and empirical results, helps to offset this limitation.

### Questions
1. What is the ratio of the training cost for RL fine-tuning compared to the training of the diffusion model?

2. Can the proposed method be combined with techniques such as gradient search [1] and local search [2], or were the empirical results already based on additional techniques during inference?

3. The paper uses the LoRA fine-tuning method. How would the results compare if full fine-tuning was used? What about the computational cost? And how do the results differ when using other fine-tuning methods?

4. Can this method be adapted to other supervised learning based models?

[1] T2T: From Distribution Learning in Training to Gradient Search in Testing for Combinatorial Optimization. NeurIPS 2023.

[2] DIMES: A Differentiable Meta Solver for Combinatorial Optimization Problems. NeurIPS 2022.

### Soundness
3

### Presentation
3

### Contribution
3
