# BEEM: Boosting Performance of Early Exit DNNs using Multi-Exit Classifiers as Experts

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Early Exit (EE) techniques have emerged as a means to reduce inference latency in Deep Neural Networks (DNNs). The latency improvement and accuracy in these techniques crucially depend on the criteria used to make exit decisions. We propose a new decision criterion BEEM where exit classifiers are treated as experts and aggregate their confidence scores. The confidence scores are aggregated only if neighbouring experts are consistent in prediction as the samples pass through them, thus capturing their ensemble effect. A sample exits when the aggregated confidence value exceeds a threshold. The threshold is set using the error rates of the intermediate exits aiming to surpass the performance of conventional DNN inference. Experimental results on the COCO dataset for Image captioning and GLUE datasets for various language tasks demonstrate that our method enhances the performance of state-of-the-art EE methods, achieving improvements in speed-up by a factor $1.5\times$ to $2.1\times$. When compared to the final layer, its accuracy is comparable in harder Image Captioning and improves in the easier language tasks. The source code is available at \url{https://anonymous.4open.science/r/BEEM1-639C/README.md}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the early exit (EE) technologies for language tasks and image captioning tasks. More specifically, instead of making decisions based on individual intermediate layers, this paper proposed to use weighted sum of multiple intermediate layers to achieve stronger results. Thresholds for each layer are set with error rate restrictions on the validation set, to make sure each exit classifier (on early exited examples) performs no worse than the final layer. Speed-up improvements are achieved on both language and image captioning tasks, while on language tasks there’s also a tiny quality boost.

### Strengths
* Extensive experiments are conducted on both language tasks and the image captioning task, with source code attached and plenty of baseline results reported.
* The proposed early exit method not only speeds up the inference, but also improves model quality on language tasks.

### Weaknesses
 * Speed-up factor is only computed based on the theoretical analysis (line 412), which is very misleading, especially for image captioning tasks where exit is only attached to the decoder but not encoder (line 201). In this case, do you count speed up only based on decoder layers? This is problematic, for example the baseline method MuE in Table3 applies early exit to both the encoder and the decoder (Figure2 of https://arxiv.org/pdf/2211.11152) and how is that calculated in line 386? Or do you also count encoder layers as a constant in this case as the inference cost is never reduced for encoders? If that’s the case, then it’s also not accurate due to the shape mismatch between the vision encoder and the language decoder. It would be more useful to report the actual end-to-end inference time speed up with and without early exit. The current speedup metric, focusing solely on decoder layers, makes comparisons with methods like MuE difficult and potentially unfair, as MuE leverages early exits in both encoder and decoder. The lack of end-to-end timing also obscures the true practical benefit of the proposed method, especially in scenarios where encoder costs are non-negligible.
* Per-layer threshold tuning depends on the validation set of each downstream task, which makes it not practical for broad use cases (e.g. zero-shot or few-shot tasks). Section 6.2 compares vallina threshold selection with the proposed threshold selection method, do you also have study showing the impact of validation set size? For example, if reduce the size of the validation set, would that significantly affect the proposed threshold setting method quality? The reliance on a validation set for threshold tuning is a significant limitation, hindering the method's applicability to scenarios with limited or no labeled data. The paper should explore the sensitivity of the threshold selection method to the size of the validation set, as this directly impacts the practical utility of the approach. A smaller validation set might lead to suboptimal thresholds, affecting both accuracy and speedup.
* The proposed method is incremental, where it differs from the baseline methods of whether or not to use a weighted sum of the exit classifiers. And there’s also no ablation test to verify this point of using a weighted sum versus using simply individual exit classifiers. It's unclear whether we should treat DeeBERT and PABEE as ablation tests because the results are produced with the existing code (line 376) instead of a comparable setup (e.g. exactly the same code from this paper). The core novelty of the proposed method, the weighted sum of exit classifiers, lacks sufficient empirical justification. While the paper presents results against DeeBERT and PABEE, these are not true ablation studies as they do not isolate the impact of the weighted sum component within a controlled experimental setup. A direct comparison of the proposed method with a version that uses individual exit classifiers would be necessary to validate the contribution of the weighted sum approach.

### Questions
* In line 412, to calculate speed-up factors for image captioning tasks, how do you distinguish the cost from the vision encoder and the language encoder / decoder? 
* Are the vision / language backbones fine-tuned or frozen (where only the new linear layers are trainable)?

### Soundness
3

### Presentation
2

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
The paper introduces BEEM, a novel framework for enhancing the performance of Early Exit Deep Neural Networks (DNNs) by treating exit classifiers as experts. The key idea is to aggregate confidence scores from these exit classifiers, making exit decisions based on the ensemble effect and consistency of predictions. A sample exits the network when the aggregated confidence exceeds a predefined threshold, which is determined by the error rates of intermediate exits. The paper presents experimental results on the COCO dataset for image captioning and GLUE datasets for language tasks, showing improvements in speed-up by a factor of 1.5× to 2.1× and comparable or improved accuracy compared to the final layer of DNNs. The significance lies in its ability to reduce inference latency while maintaining or enhancing accuracy, particularly useful for resource-constrained environments.

### Strengths
The paper introduces BEEM, a novel framework for enhancing the performance of Early Exit Deep Neural Networks (DNNs) by treating exit classifiers as experts. The key idea is to aggregate confidence scores from these exit classifiers, making exit decisions based on the ensemble effect and consistency of predictions. A sample exits the network when the aggregated confidence exceeds a predefined threshold, which is determined by the error rates of intermediate exits. The paper presents experimental results on the COCO dataset for image captioning and GLUE datasets for language tasks, showing improvements in speed-up by a factor of 1.5× to 2.1× and comparable or improved accuracy compared to the final layer of DNNs. The significance lies in its ability to reduce inference latency while maintaining or enhancing accuracy, particularly useful for resource-constrained environments.

### Weaknesses
1. The paper provides extensive experimental results demonstrating the effectiveness of BEEM in improving inference speed and accuracy across various NLP tasks and image captioning, which strengthens the credibility of the proposed method.

2. The theoretical analysis providing conditions under which BEEM outperforms standard DNN inference adds depth to the paper and offers insights into its underlying mechanisms.

3. The paper is well-organized, with clear explanations of the methodology, experiments, and results, making it accessible to readers.

### Questions
1. While the paper demonstrates strong performance on NLP and image captioning tasks, it is unclear how well BEEM generalizes to other types of tasks or datasets, which could be a limitation in its applicability.

2. The paper could provide more details on the computational complexity of implementing BEEM, especially regarding the aggregation of confidence scores and the potential overhead it introduces.

3. The performance of BEEM is highly dependent on the choice of thresholds, and the paper could benefit from a deeper exploration of how sensitive the model is to these choices.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors propose a new decision criterion, BEEM, where exit classifiers are considered experts whose confidence scores are aggregated. A sample exits when the aggregated confidence surpasses a set threshold. The paper evaluates this approach on the COCO dataset for image captioning and GLUE datasets for various transformer-based language tasks.

### Strengths
The results look promising, as shown in Tables 1, 2, and 3.

As this area is outside my expertise, I would defer to my fellow reviewers on:
- The relevance of the benchmark tasks and datasets used in the paper
- The significance of the results
- Any potential biases or issues within the experimental setup

### Weaknesses
Presentation issues:
- The introduction and abstract delve too deeply into technical details from the outset. Consider starting with a high-level overview before moving into specifics, which are available in detail later.
- Rework Figure 1: It should be consistent with other figures. For instance, S1 should connect to S2 with an arrow.
- The title of Section 3 ("Problem Setup") feels off.
- Section 3.1: The setup is challenging to follow. How are parameters denoted for exit classifiers? Are they trained independently or jointly with the model? Are the exit classifiers linear? Additionally, a brief (one-sentence) explanation of why the KL term is relevant would - improve clarity. Is the inference algorithm novel here, or adapted from previous work?
Section 3.2: Describe the task (e.g., image captioning) first before discussing specific architectures.
- Line 219: Statements like "confidence-based early exit methods like DeeBERT and ElasticBERT..." lack supporting evidence. Many claims are subjective, without empirical or theoretical backing.
- Section 3.3: The cost vector isn't "learned" in the typical sense; it's set by the model developer. Adjust the wording accordingly.
- Lines 256–259 are confusing; rephrase them. For instance, what is L? Is it the number of layers? Why is S_i < L important? What does i signify?
- In Section 3, contributions are not clearly separated from known results in the literature. Improved subsectioning could help delineate the original contributions.

Nit:
- Use \citep instead of \citet when appropriate (e.g., Line 46).
- Line 215: There's no Equation 5.
- Theorem 3.1: Avoid using t for the layer index, as it was previously used for tokens (Line 205). Clarify terms a_t and b_t, which are hard to interpret.
- Table 5 should appear after Table 4.

### Questions
The paper seems somewhat rushed, with presentation issues that would benefit from an additional round of revision (resubmission basically). From my past experiences, these are unlikely to be fully addressed during the rebuttal period. Given the positive empirical results, I believe the paper would be stronger with more attention to clarity in writing, figure design, and structural organisation.

How much are you prepared to revise the presentation of the paper? If you are aiming for acceptance, please outline a specific plan to improve its readability and structure.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
BEEM presents an approach for reducing the latency of model inference by allowing classification decisions to be made at multiple points along the model, with early termination occurring if classification confidence exceeds a threshold. Instead of treating each early exit point independently, BEEM also considers a consensus along a span of exit points to be sufficient for early exiting, even if the confidence of the current exit point is below the threshold that would allow exit by itself.

### Strengths
Treating early exiting as an ensemble based consensus mechanism is a good idea, and weighting those exit classifiers based on their ability to classify effectively is also a good idea. As best I can tell, the approach does not introduce hyperparameters without providing a rigorous way to arrive at them, which I think helps with the general utility of the approach. Given that classifiers and next-token generation are major parts of modern AI, and this approach works on both, I think this work has significance.

### Weaknesses
I don't feel like there are any showstopping weaknesses that call into question the acceptability of the paper in general. So I will limit it to some constructive feedback, and then hopefully the authors can speak to my questions below.

Figure 1:
- I found this figure a little bit hard to parse, even after reading the rest of the paper. I think that if you had an arrow from the 0.065 box to the addition operator above it, it would be much more obvious what’s happening. 

Section 3.4.2:
- Line 262.5: Should it be c_stop or c_stop^t?
- Should c_misc^t be divided by c_stop on line 264, as it’s meant to be the count (“represents the number of samples …”), and thus `c_misc^t / c_stop^t` would be the `p^t` error rate? Otherwise we’re looking at `c_misc^t / c_stop^{2 (t)}` which doesn’t seem to be right. 

Section 4:
- It perhaps would be nice to see the early exit behaviors of some of the techniques with a histogram over exit points, for example. Or even simply the average exit layer over each dataset. 

Section A.2
- Broken table link on line 782

Nit:
- Wrong parenthesis form on line 319
- If you have space, it might be good to introduce what BEEM-A and BEEM-C mean in Table 1, as it doesn’t show up until the end of section 4.1.Metric. 
- Line 445 “poo [sic]” typo

### Questions
Equation 2:
Why do we only track the max prediction chain? Alternatively, could we just continue to aggregate weighted confidences until one of them reaches threshold? For example, if the early parts of the model are trying to decide between two classes, and thus have comparable (but oscillating max) confidence, in BEEM, these oscillations cause the S_i score to stay small, and thus requiring a deeper traversal once the two classes are resolved into one (as we need to build confidence for the single resolved class).

Section 4:
Why was DNN-9L chosen? Probably a minor question, but unless that comes from a related work, I'm not sure where the 9 came from.

General:
It seems intuitive that perhaps some layers are only specifically good at EE-classifying a subset of classes. Have you observed any behavior like this? It would tie into my question about equation 2, which is that because you're relying on a chain of consistent max labels, that uneven error distributions could be harming your overall approach.

### Soundness
4

### Presentation
3

### Contribution
3
