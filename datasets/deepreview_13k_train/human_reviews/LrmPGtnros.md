# Three-in-One: Fast and Accurate Transducer for Hybrid-Autoregressive Speech Recognition

- Decision: Accept
- Scores: 6, 8, 8, 5

## Abstract
We present Hybrid-Autoregressive Inference Transducers (HAI-T), a novel architecture for speech recognition that extends the Token-and-Duration Transducer (TDT) model. Trained with randomly masked predictor network outputs, HAI-T supports both autoregressive inference with all network components and non-autoregressive inference without the predictor. Additionally, we propose a novel semi-autoregressive inference method that first generates an initial hypothesis using non-autoregressive inference, followed by refinement steps where each token prediction is regenerated using parallelized autoregression on the initial hypothesis. Experiments on multiple datasets across different languages demonstrate that HAI-T achieves efficiency parity with CTC in non-autoregressive mode and with TDT in autoregressive mode. In terms of accuracy, autoregressive HAI-T achieves parity with TDT and RNN-T, while non-autoregressive HAI-T significantly outperforms CTC. Semi-autoregressive inference further enhances the model's accuracy with minimal computational overhead, and even outperforms TDT results in some cases. These results highlight HAI-T's flexibility in balancing accuracy and speed, positioning it as a strong candidate for real-world speech recognition applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a training method to improve the performance of Token-and-Duration Transducer (TDT, Xu et al., 2023), which enables TDT to perform decoding in several different modes that improve efficiency without sacrificing performance much.

The main contributions are as follows
1. Introduce “transcript masking” as a regularization method for TDT training, which improves the regular auto-regressive decoding performance
2. Decode with “empty transcript” (ie feed entirely masked transcript to the predictor module) to greatly reduce the runtime for AR decoding. (This is referred to as non-autoregressive (NAR) decoding in the paper, but I do not agree it should be called NAR. See details in later sections)
3. A hybrid decoding approach to improve the hypothesis proposed by empty transcript decoding. In particular, it uses that hypothesis as input the predictor module, gets predictor embeddings for each text position “in parallel”, and the take the argmax from each position in parallel.

### Strengths
1. Masking target is an effective approach verified in several other models (TDS for CTC, MaskPredict for NAR translation), which can serve as a method of regularization or a way to build non-autoregressive model. Applying to TDT is a clever idea which serves both purposes.
2. Empirical results on large scale study are convincing in terms of the effectiveness of improving NAR and the more efficient decoding methods (NAR, SAR) proposed in the paper based on TDT
3. The paper also presents a good set of ablation studies (stateless / no zero duration / duration range / duration distribution analysis / argmax token analysis) to provide readers more insights on why it works and how the model behaves.

### Weaknesses
1. Technically it is not correct to call the method non-autoregressive. Despite that the predictor does not take the predicted token as input, it still depends on the duration predicted from the previous step to determine what enc[t] to compute argmax on (line 7 of Xu et al. (2023)). Hence, they cannot be fully parallel and should be still considered autoregressive. I acknowledge that runtime wise it is almost identical to NAR because argmax can be precomputed for all (t, u), but this is still wrong in terms of the nomenclature.
2. Missing discussion of limitations. For example, the refinement step cannot fix the error if the NAR hypothesis is shorter or longer than the ground truth. 
3. Missing comparison with similar or related methods. For example, how does it compare with generating top-K hypothesis with HAI-T NAR or CTC, and then rescore by an AR model
4. The argument of HAI-T being superior than RNN-T and TDT is too strong. On individual datasets it loses in quite a few cases (e22, giga, clean, other, spgi, vox). The authors should just claim on-par.

### Questions
* (Line 254) How important is it to initialize HAI-T with TDT? Are the baseline models’ encoder initialized from a PT model? What’s the performance drop for HAI-T if it is not initialized from TDT?
* Is the stateless predictor merely an embedding table?
* Has the authors compared NAR with NAR-Viterbi? How are the duration posterior and token posterior combined (ie is a weight introduce to rebalance token and duration posterior)?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the Hybrid-Autoregressive Inference Transducer (HAI-T), an extension of the Token-and-Duration Transducer (TDT) designed to support autoregressive (AR), non-autoregressive (NAR), and semi-autoregressive (SAR) inference within a single framework. The key innovation is the use of stochastic predictor masking during training, enabling seamless switching between inference modes.

AR inference follows the TDT process, while NAR inference simplifies processing by using a zeroed tensor in place of predictor outputs for single-pass decoding. SAR inference combines the strengths of both approaches, generating an initial hypothesis with NAR and refining it with AR-like processing using shifted representations. The paper also proposes a Viterbi-based decoding method to enhance results. Experimental evaluations across English and German datasets show that HAI-T outperforms CTC in NAR mode and matches or exceeds TDT and RNN-T in AR mode, with further improvements observed using Viterbi decoding.

### Strengths
**Originality**: The paper introduces a simple but effective technique: masking the predictor output 50% of the time during training, which allows the joiner to handle non-autoregressive (NAR) inference. This enables the model to support multiple inference strategies—AR, NAR, and SAR. The carefully crafted NAR and SAR inference strategies leverage the TDT architecture well and show improved performance across multiple datasets.

**Quality**: The paper provides thorough experimental evaluations across various datasets in both English and German, and includes comparisons with standard models like CTC, TDT, and RNN-T. The consistent improvements in performance across these benchmarks demonstrate the robustness of the proposed approach.

**Clarity**: The authors do a great job explaining how the AR, NAR, and SAR inference modes work, making it easier for readers to follow how HAI-T switches between different inference strategies. The inclusion of a code snippet to show how the masking is implemented during training is a nice touch that makes the paper accessible to researchers at various levels of ASR expertise.

**Significance**: The introduction of NAR inference with TDT, which outperforms CTC, and the development of SAR inference, which balances the speed of NAR with the accuracy of AR, are important contributions for real-world ASR applications where both efficiency and accuracy are needed. HAI-T effectively addresses some of the limitations of existing transducer models and sets a new standard for flexible and adaptable ASR models. This work is likely to encourage more research in hybrid inference strategies within the ASR field.

### Weaknesses
1. **Incremental Architectural Innovation**: While HAI-T's hybrid approach to inference is creative, it builds on the existing Token-and-Duration Transducer (TDT) model. The primary novelty lies in its training strategy and inference flexibility rather than any fundamental architectural innovations. This could make the contribution seem incremental. The core modification involves masking the predictor output during training, which, while effective, is a relatively minor change to the existing TDT framework. The paper does not explore more substantial architectural modifications that could potentially lead to more significant performance gains or novel capabilities beyond the hybrid inference approach.

2. **Lack of Detailed Training/Inference Specifications**: The paper omits crucial details about the training setup, such as the type and number of GPUs used, learning rates, schedules, and batch sizes. Additionally, the reported inference times lack confidence intervals and clarity on whether they were computed using a CPU or GPU. These omissions limit reproducibility and make it difficult to gauge the true computational demands of the model. The absence of specific hyperparameters and training configurations makes it challenging for other researchers to replicate the reported results or adapt the model to different datasets. Furthermore, the lack of confidence intervals on inference times makes it difficult to assess the practical speed-accuracy trade-offs of the proposed method.

3. **Dependency on Pretrained Models**: The reliance on pretrained models for initializing the encoder, which are already robust and highly optimized, raises questions about the origin of the reported performance gains. This reliance could make it challenging to separate the contribution of HAI-T's unique elements from the advantages conferred by the pretrained encoder. Furthermore, the use of an English checkpoint for initializing the German model might influence the results, yet the paper does not address this potential impact. The paper should include a comparison of the German model trained from scratch to the one initialized with an English checkpoint to fully understand the impact of the pretraining.

4. **Clarity on Limitations**: The paper would benefit from a clearer discussion of the potential limitations of HAI-T. For instance, it does not explore how the model performs under challenging conditions, such as noisy or highly varied audio inputs, or whether it would require significant adjustments to maintain performance in such scenarios. The paper should also discuss the computational cost of the SAR inference mode, which involves both NAR and AR steps, and how it compares to other approaches. The paper should also discuss the limitations of the Viterbi decoding, such as its computational cost and potential impact on inference latency.

### Questions
1. Why was the Viterbi-based decoding added as an after-thought rather than in the main experiment? By how much does it increase the inference times?

1. Could you provide more details on the training setup? The link to hyperparameters in footnote 3 gives a 404-not found error.

2. How were the inference times computed, and provide the confidence intervals?

3. Did you try training the HAI-T from scratch? Especially since you have access to a large English dataset, training from scratch should be feasible.

4. What are the potential impacts of initializing the German model with an English encoder checkpoint? 

5. When applied to data with high variability or noise, how does the model handle such conditions compared to existing approaches? 

6. Table 1 and 3 exceeds the margin, please ensure it fits within the margins.

7. The algorithms could use some refinement to avoid ambiguity in mathematical operations and naming conventions. For example `shifted_hyp` instead of `shifted-hyp`

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a simple yet effective method for training a Token-and-Duration Transducer (TDT) model by stochastically masking out the predictor. It also introduces a novel semi-autoregressive (SAR) inference mode, which first uses non-autoregressive (NAR) decoding to generate initial hypotheses and then applies autoregression to iteratively refine these hypotheses in parallel. Evaluation on multiple datasets demonstrates that the proposed method, HAI-T, achieves substantial performance gains compared to vanilla CTC in non-autoregressive mode. Furthermore, the proposed semi-autoregressive mode provides greater flexibility in balancing accuracy and speed.

### Strengths
* The paper introduces a straightforward approach that requires only a single-line change to the existing joint computation code in the Token-and-Duration (TDT) implementation and performs effectively in practice.
* Evaluations are conducted on multiple ASR corpora, including the AMI test, Earnings22, Gigaspeech test, Librispeech test-clean and test-other, Spgispeech test, Tedlium test, and VoxPopuli test.

### Weaknesses
Although the method is simple, the proposed HAI-T appears to be an incremental improvement over TDT.

* In line 259, the authors should clarify what is meant by [1-8].
* The proposed semi-autoregressive inference mode generates an initial hypothesis through NAR inference and then refines the hypothesis using the predictor. How is the proposed semi-autoregressive mode different from CTC/RNN-T-based joint decoding? Could the authors expand the discussion in the related work section?
* Please provide results for the HAI-T model without duration settings in Table 2 for a better understanding across different language settings.
* Include decoding time results using Viterbi decoding in Table 3 for completeness.
* Add x and y labels in Figure 2.
* For deeper understanding, the authors could include results on RTF and emission delays for both the proposed and baseline methods.
* A realistic comparison would include the proposed semi-autoregressive inference mode against CTC/RNN-T results in joint decoding modes.
* The results appear promising. However, a detailed breakdown of the Word Error Rate (WER) improvements with semi-autoregressive mode would be beneficial. For instance, are there notable changes in substitutions, deletions, or insertions? Which error type shows the most improvement, or are they all enhanced to a similar degree? This information could provide clearer insights into the impact of semi-autoregressive decoding.
* It is difficult to understand how the HAI-T training procedure dramatically reduces the occurrence of 0-duration predictions, given that it is trained by stochastically masking out the predictor. Could the authors expand on this phenomenon in the discussion?

### Questions
* In line 259, the authors should clarify what is meant by [1-8].
* The proposed semi-autoregressive inference mode generates an initial hypothesis through NAR inference and then refines the hypothesis using the predictor. How is the proposed semi-autoregressive mode different from CTC/RNN-T-based joint decoding? Could the authors expand the discussion in the related work section?
* Please provide results for the HAI-T model without duration settings in Table 2 for a better understanding across different language settings.
* Include decoding time results using Viterbi decoding in Table 3 for completeness.
* Add x and y labels in Figure 2.
* For deeper understanding, the authors could include results on RTF and emission delays for both the proposed and baseline methods.
* A realistic comparison would include the proposed semi-autoregressive inference mode against CTC/RNN-T results in joint decoding modes.
* The results appear promising. However, a detailed breakdown of the Word Error Rate (WER) improvements with semi-autoregressive mode would be beneficial. For instance, are there notable changes in substitutions, deletions, or insertions? Which error type shows the most improvement, or are they all enhanced to a similar degree? This information could provide clearer insights into the impact of semi-autoregressive decoding.
* It is difficult to understand how the HAI-T training procedure dramatically reduces the occurrence of 0-duration predictions, given that it is trained by stochastically masking out the predictor. Could the authors expand on this phenomenon in the discussion?

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
This paper introduces a model called HAI-T, an extension of the Token-and-Duration Transducer (TDT). TDT itself is an extension of RNN-T, where token prediction and duration prediction are decoupled. The authors propose randomly dropping the predictor network of TDT so that the model can operate in both auto-regressive (AR) and non-autoregressive (NAR) modes. They also investigate a semi-AR mode, where the NAR decoding result is refined through AR decoding.

### Strengths
The paper presents a novel idea of randomly dropping the predictor network to enable the TDT model to function in both AR and NAR modes. Especially, as far as I am aware, this is the first work to evaluate the NAR version of the TDT model.

### Weaknesses
 - Insufficient Contributions
  - The idea of randomly dropping the decoder network is quite simple, making this more of an investigation paper rather than a presentation of a highly novel idea. In this context, rigorous experimental validation is crucial, but the evaluation provided is not sufficient to substantiate their claims (see the next section).
  - The combination of NAR and AR modes -- or more generally, the combination of a faster, less accurate model with a slower, more accurate model -- has been explored extensively. The method proposed in this paper is relatively straightforward and lacks theoretical novelty. I have listed a few papers as examples, but there are many more relevant works. I suggest explicitly discussing these prior works and highlighting specific differences in methodology or performance.
    - NAR + AR:
      - H. Inaguma, et al., “Non-autoregressive end-to-end speech translation with parallel autoregressive rescoring,” 2021.
      - S. Arora, et al., “Semi-Autoregressive Streaming ASR with Label Context,” ICASSP 2024.
    - Fast + Slow:
      - J. Mahadeokar, “Streaming parallel transducer beam search with fast-slow cascaded encoders,” Interspeech, 2022.

- Insufficient Evaluation
  - The authors claim that the proposed method outperforms RNN-T and TDT in AR mode, but their experimental evidence is not convincing. In the first 7 rows of Table 1, the AR mode results for RNN-T, TDT, and HAI-T (the proposed model) average 7.15%, 7.13%, and 7.10%, respectively. The difference from 7.13% to 7.10% is too minor to definitively demonstrate HAI-T's superiority. Moreover, when examining individual test sets like “ami” and “e22,” the proposed model often underperforms compared to RNN-T and TDT. It is likely that there is no statistically significant difference between TDT and HAI-T in AR mode, and the observed difference may be due to random fluctuation (e.g., the trend could easily reverse with additional testing data). More extensive experiments with statistical significance tests over multiple evaluation sets are suggested.
  -  Additionally, while the authors show that the HAI-T model performs better with a “stateless” decoder or when excluding 0-duration configurations in the remaining 8 results of Table 1, the same configurations should have been applied to the baseline models for a fair comparison.
  - The authors claim that their proposed method outperforms CTC in NAR mode, but this is not convincingly demonstrated. In the NAR setting, the HAI-T model slightly outperforms CTC (7.38% vs. 7.19%) but with a slight increase in computational overhead (41 vs. 39 in time). While the increase in time is minor, the improvement in WER is also small, raising concerns that the improvement may simply be due to increased parameters. 
  - Additionally, the paper does not define the term “time,” which presents another issue. Please explicitly define how "time" is measured (e.g., wall clock time, CPU time, number of operations) and under what conditions (e.g., hardware specifications, batch size) instead of merely mentioning Huggingface ASR leaderboard.
  - It would be beneficial to include the “time” metric in Table 3.

- Description Issues
  - The descriptions of their “code (page 4)” and “algorithm (page 5)” are inadequately defined.
    - The code on page 4 seems unnecessary. The algorithm is simple enough that additional explanation is not required.
    - The algorithm on page 5 relies on hidden assumptions known only to the authors. For example, (1) it is unclear what the output of the “joint” function is, and why the second output is omitted, and (2) the application of “dim=-1” in argmax assumes a specific shape of “token-probs,” which remains undefined. Please make the algorithm self-contained by appropriately defining each notion.
  - The decoding strategy used for NAR-mode is unclear.
    - From the explanation in Section 4.1, it appears that the authors still applied a decoding algorithm used for TDT even when the model is used in NAR mode. I have several questions:
      - I assume that the decoding algorithm is still left-to-right. If this is the case, can it still be called "NAR"? Please explicitly define the notion of NAR in the paper.
      - Is there any notion of a 'beam' in the decoding algorithm for HAI-T? This is a clarification question, and I guess the answer is no. However, if beam search decoding was used, the configuration needs to be specified. In addition, if all experiments were conducted without beam search, it is still highly recommended to evaluate each method using the beam search configuration, as it is the most widely used.
      - What decoding algorithm is used for CTC (best path, prefix search)? Can the author provide the impact of decoding algorithms (not only for CTC, but also for RNN-T with beam size) to understand the impact of it?
    - In Section 6.2, the authors suddenly introduce Viterbi-based decoding in the experimental section. They should have described the details of the decoding strategies (both the one in the main experiment and Viterbi decoding) in the proposed method section to clearly show the differences between them. It would have been better to explicitly describe Algorithm 2 of Xu et al. (2023) instead of merely referencing it, as the algorithm is not widely known within the community. Including the memory footprint is also highly recommended, as Viterbi decoding may require significantly more memory during inference, especially for long input durations.
  - The discussion in Section 6.3 is unclear to me. The authors claimed that "the ability to skip more frames enables the model to learn better representations" by presenting Table 4 with different max-duration settings, where the shorter max-duration setting provided worse results. However, isn't it just showing that the shorter max-duration is not able to capture the real duration distribution? I think that the only conclusion we could draw from Table 4 is "the max duration needs to be sufficiently large to represent the real distribution," and their claim that "the ability to skip more frames enables the model to learn better representations" cannot be drawn.

### Questions
Please address the concerns and questions raised in the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2
