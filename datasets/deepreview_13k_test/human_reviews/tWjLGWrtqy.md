# MOSAIC: Multiple Observers Spotting AI Content, a Robust Approach to Machine-Generated Text Detection

- Decision: Reject
- Scores: 3, 5, 8, 5, 6

## Abstract
The dissemination of Large Language Models (LLMs), trained at scale, and endowed with powerful text-generating abilities has vastly increased the threats posed by generative AI technologies by reducing the cost of producing harmful, toxic, faked or forged content. In response, various proposals have been made to automatically discriminate artificially generated from human-written texts, typically framing the problem as a classification problem. Most approaches evaluate an input document by a well-chosen detector LLM, assuming that low-perplexity scores reliably signal machine-made content. As using one single detector can induce brittleness of performance, we instead consider several and derive a new, theoretically grounded approach to combine their respective strengths. Our experiments, using a variety of generator LLMs, suggest that our method effectively increases the robustness of detection.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a new method to increase the robustness of detecting artificially generated text from large language models (LLMs). The authors argue that the current detection methods are fragile and can be easily misled by changing the generator or the associated sampling method. They propose an ensemble method that combines the strengths of multiple LLMs to detect forged texts. Using fundamental information-theoretic principles, they derive an algorithm that identifies time-varying mixture models to minimize the worst-case expected encoding size. This approach eliminates the need to search for the best detector(s) empirically and allows for the smooth addition of new models as they become available. The method is tested on standard benchmarks and a new corpus of machine-generated texts, proving its effectiveness in robustly identifying a variety of generators.

### Strengths
1) The paper's originality lies in its theoretical grounding and its method of combining multiple detectors, as opposed to relying on a single detector, which can lead to brittleness.
2) The quality of the research is evident in the rigorous experiments carried out, which used a variety of generator LLMs and both standard and new benchmarks. 
3) The paper's significance lies in its potential to increase the robustness of artificial text detection systems, thereby addressing a key challenge in the field of generative AI technologies.

### Weaknesses
1) The baseline results are significantly different from the findings shown in Figure 3 of the Binoculars report by Hans et al., 2024, prompting doubts regarding the reliability of the experiments.
2) The experimental findings do not validate the superiority of the method. In particular, as Table 3 shows, MOSAIC-4 (avg) only excels in 1 out of 12 datasets, and MOSAIC-4 (unif) only surpasses in 3 out of 12 datasets, implying that the method compromises detection accuracy for the sake of robustness.
3) The method fails to tackle the issues of brittleness and the need for revisions, as pointed out in LN050. Specifically, as Table 4 shows, after the integration of the generator LLM, MOSAIC-4 (avg) demonstrates improved detection accuracies, indicating that the method still struggles with brittleness and necessitates adjustments when new generators are introduced.

### Questions
LN058: Why is there a requirement for time-varying mixture models? Shouldn't the language models used remain consistent regardless of the text source?

LN059: Can you provide an intuitive explanation as to why we need to minimize the worst-case encoding size?

Figure 1: Does \miu represent the probability assigned to each token?

LN332: The statement might not be accurate. In my understanding, FastDetectGPT and DetectGPT, despite their similar names, differ substantially in their principles and performance. DetectGPT creates minor perturbations, whereas FastDetectGPT doesn't generate tokens, but rather computes the detection metric from the predictive distribution.

Table 2: The results significantly differ from the findings presented in Figure 3 of the Binoculars report (Hans et al., 2024), which raises questions about the thoroughness of the experiments.

Table 3: MOSAIC-4 (avg) only outperforms in 1 out of 12 datasets, and MOSAIC-4 (unif) only outperforms in 3 out of 12 datasets. Does this suggest that the method achieves robustness at the cost of detection accuracy?

Table 4: MOSAIC-4 (avg) shows good detection accuracies after incorporating the generator LLM. Does this imply that the method still has issues with brittleness and requires revision when new generators become available?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work addresses the problem of detecting machine generated text.
Past work focused mostly on a set of text generated by a single model, which made any detector susceptible to overfit to that model while in the wild the identify of the generated model might be unknown.
This paper removes that assumptions and achieves good results by relying on a mixture of judges which are combined through an iterative algorithm that instantiates a larger family of classes known as "Blahut–Arimoto".

### Strengths
* a more realistic assumption of a problem that is becoming more widespread in a variety of areas
* good scores on various (6) benchmarks of various sizes and languages

### Weaknesses
1) the paper itself is not self-contained as the algorithm is not properly explained and one needs to refer to Appendix B for those unfamiliar with it (most of the readers?)

2) the presentation of the final results is weak (3 tables) and one needs to navigate across tables in different pages (Table 2 & 3) to see the difference. A graph would be more informative

3) while hard to interpret (see 2) ), it seems that the proposed method often underperforms existing methods, while being computationally more expensive (??). The interpretability features of looking into the respective weights, as well as the robustness is still compelling, but if this is not reflected in the final performance it would be important to explain


Two references which the authors might want to consider: https://arxiv.org/abs/2404.18796 for the idea of using a panel of experts, and https://arxiv.org/abs/2111.02878 for an early work on machine detection not relying on perplexity

### Questions
* one would expect that that more iterations for Blahut–Arimoto, the higher the final performance. Is this the case? A graph with performance over number of iterations would be very informative
* most of the numbers seem very close. Do the algorithms all detect the same documents? Your algorithm in particular is different than the others as it relies on a panel of judges, could you provide some error analysis?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
MOSAIC introduces a new ensemble approach that combines several detector models to spot AI-generated texts. The method enhances the reliability of detection by integrating insights from multiple models, thus addressing the limitations of using a single detector model which often results in performance brittleness. This approach also involves using a theoretically grounded algorithm to minimize the worst-case expected encoding size across models, thereby optimizing the detection process.

### Strengths
1. By using multiple models, MOSAIC reduces dependency on a single model's performance, thus offering greater stability against various adversarial tactics or novel AI text generators.
2. The method leverages solid theoretical models to optimize performance, potentially leading to more consistent and reliable detection across different datasets and AI generators.
3. The ensemble approach allows for the integration of new models as they become available, supporting scalability and adaptation to new threats and technologies.

### Weaknesses
The manuscript is generally well-crafted. However, some concepts and figures could benefit from additional clarification to enhance the reader's comprehension.

### Questions
1. 1. Lines 54-64, could you please define (or further explain) the term 'robustness' in a machine-generated text detection problem?
2. In Figure 1, the caption should provide an explanation of the pipeline's operation. It needs to define μ and describe how the Logits are transformed into features of the mixture model.
3. Line 95, does the circle operator o in the definition of the output space y represent a concatenating operation?
4. Section 3.1 mentions that the experiments involve some imbalanced datasets. Could you please discuss whether these imbalances are tolerable, or specified rebalance techniques are required?
5. Section 4.1 mentions the use of Blahut-Arimoto weights. Briefly introducing how are these weights calculated, and what specific role they play in adjusting the contributions of individual models within the ensemble might be helpful for readers.
6. Further discussion is needed on how the choice of tokenization and preprocessing methods affects detection accuracy. Can the proposed method be adapted to incorporate other detection models? Are there any limitations on the types of models that can be integrated?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel AI-generated text detection strategy through an ensemble of generator LLMs and also proposes their mathematical formulations, along with some experimental results suggesting its robustness.

### Strengths
1. This paper is decently presented, conveying a clear derivation and motivation, as well as an intuitive description of the underlying method. Analysis in section 4.2 is also very interesting.
2. The idea itself is very interesting and intuitive, with much mathematical implications that seem to guarantee robustness.
3. Also love that the authors have experimented with multiple datasets, including augmenting the Binocular datasets, which show efforts to establish robust evaluation of their method.

### Weaknesses
1. My first main criticism for the paper is that I am slightly incredulous of the results and the ensemble used. I feel like for a fair comparison, the authors should use the same suite of models as used in the baseline models. For instance, Binocular score uses Falcon-7b and Falcon-7b-instruct, yet MOSAIC uses TowerBase and Llama-2. Maybe the results would be more convincing they have also tried MOSAIC with Falcon models, since the superiority of MOSAIC on some domains could arise from the difference in the underlying models. Could the authors please justify more their usage as to why they did not maintain the same set of models? I am moderately confident on this and am willing to discuss more!

**Suggestion**: add experiments of MOSAIC with Falcon as the base models, and I will consider raising the scores.

2. My second main criticism is that the improvement of MOSAIC over other methods is not so salient. It seems that although MOSAIC-4 has higher average AUROC than the Binocular score by 0.2, this can be attributed to Binocular score’s crack on multilingual data. I think this might tie to my first criticism and to Binocular’s dependence on Falcon-7b, because Falcon-7b is trained on RefinedWeb, an English pretraining dataset, which causes it to have low multilingual capabilities. Aside from M4, MOSAIC-4 doesn’t do better than the baselines on RAID and Ghostbusters. Therefore, I think the results are not super convincing.
    - A minor point related to this: consider merging table 2 and 3? It would be easier for readers to compare the results.

3. My third main criticism is that this method lacks testing against adversarial attacks. How robust is it against perturbation (insertion, paraphrase, deletion) and reordering? Or is there a certain range of passage length that the method is bad at?

**Suggestion**: consider adding ablation study with adversarial attacks.

4. Minor point: There’s still some room of improvement in the paper presentation. The abstract can be also improved to describe the method in more details and to intrigue the readers. Also, I don’t necessarily agree with the statement in the abstract: “Most approaches evaluate an input document by a well-chosen detector LLM, assuming that low-perplexity scores reliably signal machine-made content.” The authors themselves have experimented with non-PPL based methods, and there are also watermarking methods. But these are minor concerns to me.

### Questions
### Question:

1. What is the run-time of this algorithm compared to the baselines?

### Typos: 
Do not affect my rating. Just kind reminders :)

1. L332 FastDetectGTP → FastDetectGPT
2. Consider using Llama-7b instead of Llama-7-b ? (e.g. line 421)
3. L446 should use “increases” and “decreases”

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MOSAIC, a novel approach to detecting machine-generated text by combining multiple language models' perplexity scores through a theoretically-grounded ensemble method. The authors derive an optimal combination algorithm based on information theory principles that maximizes mutual information between models. They evaluate their method across multiple datasets spanning different domains and languages, demonstrating improved robustness compared to existing detection approaches. The theoretical framework generalizes perplexity-based approaches and can incorporate new models smoothly as they become available. Their experiments show that MOSAIC effectively detects texts from various generators while requiring no training data, making it particularly suitable for real-world deployment.

### Strengths
1. The paper's theoretical foundation in information theory provides a principled approach to combining multiple detectors. Rather than relying on heuristic combinations, the authors derive an optimal weighting scheme using the Blahut-Arimoto algorithm that maximizes mutual information. This mathematical rigor sets the work apart from existing ensemble methods.

2. The extensive experimental validation across multiple datasets (RAID, Ghostbuster, Binoculars, M4, academic papers) demonstrates the method's versatility. The evaluation spans different languages, domains, and generator models, with MOSAIC showing consistent improvements over baselines, achieving up to 97.6% accuracy on some benchmarks.

3. The method is zero-shot and requires no training data, making it immediately applicable to new detection scenarios. This is particularly valuable given the rapid evolution of language models and the difficulty of obtaining training data for new generators.

### Weaknesses
1. The computational cost of running multiple language models for detection is significant but not thoroughly addressed. While the paper acknowledges this limitation briefly, a more detailed analysis of runtime requirements and potential optimizations would strengthen the practical applicability of the approach.

2. The method struggles with detecting texts from fine-tuned models, as demonstrated by the poor performance on the academic paper dataset (42.1% AUROC). The authors could explore incorporating domain-adapted models into the ensemble to address this limitation.

3. The paper's treatment of sampling methods' impact on detection is limited. While they observe that nucleus sampling affects detectability, a more systematic exploration of how different sampling parameters influence the method's performance would be valuable.

4. The choice of baseline models in the ensemble appears somewhat arbitrary. The authors could provide clearer criteria for selecting which models to include, especially since they show that adding weak models (like unigram) can be detrimental to performance.

### Questions
1. Have you explored methods to reduce the computational overhead of running multiple models, such as model distillation or selective invocation of ensemble members based on confidence thresholds?

2. Your analysis shows that Tower-Base models receive higher weights for non-English text detection. Could this insight be used to develop adaptive ensembles that automatically select the most appropriate models based on the input characteristics?

3. How sensitive is the method to the number of models in the ensemble? Is there an optimal ensemble size beyond which adding more models provides diminishing returns?

### Soundness
3

### Presentation
2

### Contribution
3
