# Were RNNs All We Needed?

- Decision: Reject
- Avg Score: 5.00
- Scores: 8, 6, 3, 3

## Abstract
The introduction of Transformers in 2017 reshaped the landscape of deep learning. Originally proposed for sequence modelling, Transformers have since achieved widespread success across various domains. However, the scalability limitations of Transformers—particularly with respect to sequence length—have sparked renewed interest in novel recurrent models that are parallelizable during training, offer comparable performance, and scale more effectively.
In this work, we revisit sequence modelling from a historical perspective, focusing on Recurrent Neural Networks (RNNs), which dominated the field for two decades before the rise of Transformers. Specifically, we examine LSTMs (1997) and GRUs (2014). We demonstrate that by simplifying these models, we can derive minimal versions (minLSTMs and minGRUs) that (1) use fewer parameters than their traditional counterparts, (2) are fully parallelizable during training, and (3) achieve surprisingly competitive performance on a range of tasks, rivalling recent models including Transformers.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces minimal Long Short-Term Memory (minLSTM) and minimal Gated Recurrent Unit (minGRU) models.
The authors modify the traditional LSTM and GRU models by removing dependencies on prior hidden states from the gating mechanisms, enabling parallelization through a method similar to approaches in linear RNNs and state-space models.
The changes to the gating mechanisms significantly alter how minLSTMs and minGRUs are expected to function when compared with LSTMs and GRUs, but it allows for efficient computation without the limitations that result from back-propagation through time.
Comparisons are made with state-of-the-art models, including the state-space model Mamba. 
Empirical results demonstrate that the minLSTM and minGRU models achieve competitive performance on the selective copy task, multiple reinforcement learning tasks, and a language modeling task based on the Shakespeare dataset.

### Strengths
The core idea of creating minimal versions of LSTM and GRU models for efficient parallel training is compelling.
I believe this contribution is novel and could be highly useful.
The benchmark results are encouraging and the comparisons made with other models seem appropriate.

### Weaknesses
As the authors point out, computational restrictions prevent them from providing large-scale experiments. I would be curious to see performance on additional benchmarks, such as WikiText103, Pile or the long range arena. However, I still believe the submission is strong without them.

Small typo: line 370, should read '... recurrent sequence models that can *be* trained in parallel ...'

in B.1, parallel_scan_log: log_x0_plus_b_star is not defined, should this be log_h0_plus_b_star?

in B.3.1 the pseudocode takes x_t but the code uses x 

For the purposes of reproducibility, providing anonymized code in the supplementary material would strengthen the submission.

### Questions
Under "Parameter Initializations" you state that minLSTM and minGRU are stable with default initialization, in contrast to the specialized initializations in prior linear RNN papers. Did you perform any studies using different initialization methods?

When trying to replicate minGRU using the log-space pseudocode I am struggling to get the sequential and parallel modes to match, could this pseudocode be checked through? (update: I managed to do it using the cited paper, but I think the pseudocode provided is incorrect)

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates simplified versions of traditional recurrent neural networks (RNNs), specifically LSTMs and GRUs, adapting them for efficient training by removing their hidden state dependencies, enabling parallel training. The proposed **minLSTM** and **minGRU** models retain the functional structure of their predecessors but omit time dependencies in their gates, reducing parameter count and improving computational efficiency. Empirical tests indicate these models achieve comparable performance to contemporary state-of-the-art sequence models, suggesting that streamlined versions of older RNN architectures may offer viable alternatives in sequence modeling tasks.

### Strengths
- The approach effectively repurposes older RNNs by leveraging simplifications that enable parallel training, providing an interesting contrast to complex, modern architectures.

- The proposed models significantly reduce training time, achieving speed improvements of up to 175x for sequence lengths of 512, which is a notable practical advantage.

- This work challenges the abandonment of RNNs in favor of more recent architectures and suggests potential for simpler, more interpretable models in long-sequence processing.

### Weaknesses
 *Insufficient Comparison Context:* From the current text, it is not clear whether the computational comparisons (Figure 1) were carried on considering the fact that the proposed models potentially require more layer to achieve competitor quantitative performances on tasks (Table 1). This fact potentially skews the results if competitors require fewer layers for comparable performance.

*Limited Dataset Representativeness:* The model's evaluation primarily relies on synthetic, simplified datasets, which are not representative of those used in current literature benchmarks (see Section 7/Table 4 in  [3]). This limits insights into the model’s scalability and ability to handle real-world data complexities (and it is not clear whether this was caused by memory requirements drawbacks). Moreover, the removal of hidden state dependencies from gates raises concerns regarding the model ability to preserve long range dependendencies - something that should be investigated. 

*Literature Comparisons and references:* The paper references but does not thoroughly compare against xLSTM, a similar recent work aimed at improving LSTM performance. A more detailed theoretical (at least) comparison with xLSTM would strengthen the paper's argument for minLSTM's contributions. Moreover, the paper is inspired and puts emphasis (even in the title) on the recent **resurgence** of RNNs - a concept that was highligthed by recent surveys [2,3] that could help the reader better contextualize the work.  In the aforementioned surveys, other very related works [4,5] are described that should be at least mentioned 

### Questions
1. **Layer Depth in Computational Comparisons:** (Please refer to Weaknesses) Were the computational benchmarks (Figure 1) conducted with models having comparable quantitative performances? The paper could benefit from a comparison on computational complexity normalized by model performances or depth. 

2. **Parameter Matching for Competitors:** Related to previous question. When taking results from other papers (as reported in the Appendix), were the competitor models matched in terms of parameters and model size? Variability in model configurations could impact the validity of performance comparisons.

3. **Choice of Datasets:** The model is mainly tested on very simple datasets (mostly synthetic) that are not very representative for the current literature (see [3]). The authors should comment on why this choice taken.  If the model cannot scale to large datasets due to its inner working and memory requirements (as reported in the Limitation section), this is something that hinder the paper contributions.  For instance, the Long Range Arena benchmark has became a standardize framework to test sequence models performances, that could help also in identifying the model ability to preserve long term dependencies -- that is something extremely requested by current literature. The removal of time dependecy questions the model ability to perform in such benchmarks, which I believe should be better investigated. Thus,  at least a discussion on this is required. 

4. **Theoretical Comparison with xLSTM [1]:** Could the authors elaborate on the theoretical distinctions and advantages of minLSTM over xLSTM, especially in terms of efficiency and sequence modeling?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces minimal variants of LSTM and GRU (minLSTM and minGRU) that enable parallel training via the parallel scan algorithm. Key modifications include removing hidden state dependencies and rescaling mechanisms in the LSTM. The authors demonstrate competitive performance with modern architectures on several tasks.

### Strengths
The paper's technical exposition is clear, offering good motivation for removing parts of the RNN architectures. The authors provide thorough motivation for each architectural decision, especially regarding the time-independence properties of their models. The connection to parallel scan algorithms makes sense.

The architectural innovations demonstrate consideration of practical implementation challenges. The rescaling mechanism in minLSTM ensures time-independence while maintaining model expressivity. The authors have given careful thought to numerical stability issues, providing both standard and log-space formulations of their approach. It is nice to see the PyTorch implementation details, which help to make the algorithm very concrete.

The experimental validation covers a range of tasks and provides evidence of training speed advantages wrt traditional RNNs. The performance on the selective copying task is particularly impressive, demonstrating the model's ability to handle a particular type of long-range dependencies.

### Weaknesses
The most significant concern is the paper's relationship to prior work, specifically Martin & Cundy (ParalleIizing Linear Recurrent Neural Nets over Sequence Length, ICLR 2018), which appears to have developed very similar ideas. The proposed minGRU architecture appears mathematically equivalent to their GILR architecture when \(g_t = 1 - z_t\) and \(i_t = \tilde{h}_t\) in the authors' notation. The parallel scan approach for training is also very similar. While the LSTM rescaling mechanism appears novel, this substantial overlap significantly reduces the paper's claimed novelty.

The experimental evaluation, while broad, has several limitations. The benefits over baselines are modest in most tasks, with the exception of the selective copying task, which seems carefully chosen to showcase the method's strengths. The language modeling evaluation relies solely on the Shakespeare dataset, which is both too small by modern standards. This choice of dataset is not representative of real-world language modeling challenges, which typically do not have overfitting as a major worry.

The methodology would benefit from more thorough analysis in several areas. The authors could strengthen their contribution by providing more extensive ablation studies on their architectural choices. The paper would also benefit from a clearer discussion of scaling behavior, to indicate if this architecture could be a potential replacement for transformers or Mamba at the larger scales of modern models.

### Questions
Can the authors provide a detailed comparison with Martin & Cundy (2018), specifically addressing how minGRU differs from GILR, if at all, and what novel contributions this work makes beyond the prior work? Additionally, it would be valuable to understand why these ideas are being revisited now and what new insights are gained.

How do the proposed new architectures fare at larger data sizes? How do these models perform on standard language modeling benchmarks? Results on datasets with training sequences longer than 1000 steps would be particularly good to see. Understanding the scaling behavior on modern language modeling tasks is crucial for assessing the practical value of this approach.

Finally, more detailed inference speed comparisons would strengthen the paper. How do minGRU and minLSTM compare with Mamba and traditional LSTM/GRU implementations across different sequence lengths and batch sizes?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Transformers are expensive to run on long sequences due to their quadratic complexity. Traditional RNNs such as LSTMs and GRUs have cheaper inference costs, but they cannot be parallelized during training. This paper shows how we can minimally modify these architectures to train them with parallel scans. This greatly reduces training runtime, while still maintaining good empirical performance (as demonstrated on small scale reinforcement learning and language modelling tasks).

### Strengths
The paper is well written and easy to follow. It convincingly demonstrates the speed benefits of min LSTM and GRU over their sequential counterparts.

### Weaknesses
I am afraid that the paper is half a year to one year late. Both the xLSTM (Beck et al. 2024) and the MatMul-free (Zhu et al. 2024) papers leverage a similar insight to the one of this paper, that is removing everything in LSTM/GRUs that cannot be parallelized during training. Those papers demonstrate the effectiveness of this approach at a larger scale (more than 10x the number of parameters). In addition to that, detailed comparison to these works is missing. For these reasons, I think the paper requires heavy modifications (e.g. more detailed experiments, at a larger scale) before being accepted.

### Questions
If my arguments above are valid, I don't have any question that can change my opinion of the paper.

### Soundness
4

### Presentation
4

### Contribution
1
