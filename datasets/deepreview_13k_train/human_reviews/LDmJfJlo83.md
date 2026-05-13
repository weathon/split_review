# Uncertainty Quantification with Generative-Semantic Entropy Estimation for Large Language Models

- Decision: Reject
- Scores: 6, 5, 5, 1

## Abstract
In recent years,  powerful foundation models, including Large Language Models (LLMs) and Large Multi-Modal Models (LMMs) have ushered in a new epoch of multi-faceted, intelligent conversational agents. Despite their significant early successes and widespread use, foundation models nevertheless currently suffer from several critical challenges, including their lack of transparency and predilection for "hallucinations."  To this end, we introduce Generative-Semantic Entropy Estimation (GSEE), a model-agnostic algorithm that efficiently estimates the generative uncertainty associated with foundation models, while requiring no additional auxiliary model inference steps. In principle, for any foundation model input data, e.g., a text prompt, image, text + image, etc., GSEE numerically estimates the uncertainty encapsulated in the internal, semantic manifold of the LLM generated responses to the input data. In this way, high uncertainty is indicative of hallucinations and low generative confidence. Through experiments, we demonstrate the superior performance of GSEE for uncertainty quantification (UQ) amongst state-of-the-art methods across a variety of models, datasets, and problem settings, including: unbounded language prompting, constrained language prompting, high/low generative stochasticity, acute semantic diversity prompting, and as a barometer for hallucination/predictive accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a method to evaluate the uncertainty of a language model, namely GSEE.
Specifically, the method generates a few outputs from an input prompt, then the method calculates the length-normalized spectral entropy of those outputs' semantic as the uncertainty.
The paper further evaluates the proposed methods under varied settings and compares the proposed method with baselines to show the superior performance of the proposed method.

### Strengths
(1) The paper gives a straightforward method to calculate the uncertainty of a language model and gives good illustration and intuition in Fig. 1.

(2) The paper empirically shows the proposed method works well under varied settings.

### Weaknesses
 (1) It's a bit weird for me since the uncertainty is calculated based on a set of outputs. I'm not familiar with the literature but I have seen some papers working on uncertainty estimation which estimates the uncertainty of a particular output/generation. I feel it makes less sense to estimate the uncertainty of a set of generations since we usually just care about the uncertainty of a particular generation. (I acknowledge that it makes sense to estimate the uncertainty of a set of generations if we care about the uncertainty in a set of generations.)

### Questions
As weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Generative-Semantic Entropy Estimation (GSEE), a model-agnostic algorithm for uncertainty quantification (UQ) in large language models (LLMs) and multi-modal models. GSEE estimates predictive uncertainty by analyzing the spectral entropy of covariance matrices derived from the latent embeddings of multiple generated responses. This approach aims to detect hallucinations and low-confidence predictions by measuring semantic diversity.

### Strengths
1. The method introduces a new approach to UQ by leveraging spectral entropy of covariance matrices derived from latent embeddings of generated responses. 
2. GSEE’s model-agnostic design makes it applicable across various foundation models without the need for additional natural language inference (NLI) steps, enhancing its usability and adaptability to different contexts and models. 
3. The paper provides a well-rounded evaluation of GSEE across multiple datasets

### Weaknesses
1. The method relies on latent embeddings extracted from penultimate layers, yet the impact of this choice is not examined. A detailed ablation study on embedding layer selection could clarify whether GSEE’s performance is sensitive to embedding depth, and if alternative embeddings could improve its accuracy. Specifically, the paper does not explore if earlier layers, which might capture more general semantic features, or later layers, which may be more task-specific, would yield different uncertainty quantification results. This is crucial because the quality of the covariance matrix, and thus the spectral entropy, is directly dependent on the representational power of the chosen embeddings.
2. Despite claiming efficiency, GSEE’s use of multiple generations and covariance calculations could be computationally intensive for larger datasets or more frequent real-time applications. The paper lacks a clear analysis of the computational costs and memory overhead of GSEE, which could hinder its scalability. The computational cost of generating multiple responses, extracting their embeddings, and then calculating the covariance matrix and its spectral entropy is not trivial, especially when compared to simpler methods that might rely on single forward passes or token probabilities. The paper should provide a breakdown of the time complexity for each step.
3. The presentation can be unclear and should be improved.

### Questions
Can the authors provide more details on the computational costs associated with GSEE, especially in comparison to simpler UQ methods? Insights into the time and memory complexity of GSEE could help clarify its practicality for large-scale deployment.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces Generative-Semantic Entropy Estimation (GSEE) to efficiently estimate uncertainty in generative models without requiring auxiliary model inference steps. GSEE numerically captures the uncertainty based on the spectral entropy of the covariance matrix of the generated outputs, linking high uncertainty to potential hallucinations and low confidence. The authors demonstrate that GSEE outperforms other uncertainty quantification (UQ) methods across various prompting conditions and models

### Strengths
(1) The effectiveness of applying GSEE to measure the semantic self-consistency in model responses has been demonstrated by extensive experiments on LLMs and LMMs.  

(2) It is novel to design the experiments “constrained language prompting” and “high stochasticity conditioning” to showcase the good performance of GSEE.

(3) The paper is well-written and accessible

### Weaknesses
 (1) How would this uncertainty estimation metrics GSEE enhance the trustworthiness of generated outputs? For instance, could it be effective in detecting hallucinations and how does it perform? Additionally, what is the performance of using the GSEE to predict the accuracy of the output? Could you please show some examples or use experimental results to support the claim that the GSEE could be beneficial in hallucination detection and improving the prediction accuracy?

(2) What are the advantages of GSEE compared with other metrics like semantic entropy [1], which also measure the uncertainty from the semantic perspective.

(3) Is the GSEE metric sensitive to the number of generated responses M and temperature? It seems that as more responses are generated, the diversity among them would increase, potentially affecting the stability of the GSEE.

(4) The novelty of the definition of the metric is limited, as it relies on the existing metric to quantify the semantic diversity.

### Questions
Please see the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper introduces GSEE, a method to estimate the semantic uncertainty of (vision) language models.
The method uses information in the internal state of the model to measure semantic uncertainty.
It is evaluated on four benchmark tasks, two pure language, two vision language tasks, using four different model architectures.

### Strengths
The idea of using the entropy instead of the determinant of the covariance matrix is a reasonable extension of the prior work of Chen et al.
The authors investigate both pure language as well as vision language models.

### Weaknesses
### Major:

*   The framing of GSEE being model agnostic is misleading, as it is complety reliant on the quality of the extracted answer embeddings. 
I am actually not aware of any method for UQ in LLMs/LMMs that would not be model agnostic as by this definition.
*   I don't see how step (1) for GSEE in the introduction (line 51) should ever by possible. 
It states that "Given an input datum ... we render multiple text outputs with the generative model through a single forward pass;".
I am not aware of any method to generate even one output sequence (consisting of more than one token) with a single forward pass, let alone multiple.
How it is described in line 126, it seems the usual setting of generating M sequences is used, with the expense of M forward passes times the lengths of individual sequences.
*   How is GSEE "mathematically-principled" as claimed in line 61? There is no derivation of any technical analysis, solely an empirical evaluation of an ad-hoc measure.
This is not necessarily bad, if it works well in practice, however the claim of being principled is definately not backed up by what is presented in the paper.
*   Since when is GPT3 an open-source LLM (line 196/197), available through HF transformers?
*   I am completely lost in understanding section 4.3. 
First, I don't understand the basic rationale behind introducing those "bad prompt" settings. 
Second, why is there a need to "bound" prompts? 
Aren't they given a priori, thus are completely under control of the experimentor?
Third, why are those experiments evaluated using summary statistics over the proposed uncertainty measures and do not use the PCC as for the main experiments?
*   Critical experimental details are missing. E.g. what output sequence (of the M sequences) is actually used to evaluate correctness? The most likely one? 
*   How does one know, that the latent representation captures semantics? 
Is there any investigation regarding this, e.g. comparing GSEE scores for handcrafted lexically diverse but semantically similar vs. semantically diverse but lexically similar answers?
Otherwise, it is a very strong claim that the latent space captures the semantics of a sentence well and that the eigenvectors correspond to different semantics rather than lexical structure, which I don't buy without evidence.
*   In the ablation section, line 365, there is a statement that "comparable gains were however less pronounced for baseline UQ methods". 
I didn't find the corresponding results anywhere, table 6 ony provides results for GSEE.
*   The choice of baselines is very limited. There is a lot of work on semantic entropy (Kuhn, Aichberger, Farquhar, Duan, Bakman) that has very good performance but is not compared to.
Looking at the paper of Chen et al., which is very heavily cited reveals that they used those same baselines without adapting to improvements in those last two years.
Also, length normalization for predictive entropy is not without debate, adding the non normalized variant costs basically nothing yet would give more credibility to the experiments.
*   Many things are not defined, e.g. is $\Sigma_N$ the same as $\Sigma$ or is there any difference? 
Is $\Sigma_N$ normalized to make it a "probability distribution" for calculating the entropy? 
How is the entropy actually calculated, e.g. only upper triangle or full matrix flattened?
*   I don't get the reason for dividing the entropy term by the mean length. 
The semantic embeddings $z$ are already averaged, thus do not contain any length information? 
This term rather induces length information in the uncertainty measure.

### Minor:

*   Overall, the manuscript is very hard to follow. 
Consider streamlining the choice of wording, I often had to stop thinking about whether or not two things actually mean the same or not (e.g. prompting and conditioning in section 4.3).
*   The naming "Generative-Semantic entropy estimation" is not optimal, given the well established "Semantic Entropy" method (Kuhn, Aichberger, Farquhar).


### Questions
See major weaknesses. Additionally:

* Most prior work (e.g. Kuhn, Aichberger, Farquhar, Bakman, Duan) except Chen et al., this work is heavily based upon, uses AUROC/AUPR of being correct as evaluation metric for their uncertainty measure.
Why is using the PCC better than those established measures?

---
## References:

Chen, C., Liu, K., Chen, Z., Gu, Y., Wu, Y., Tao, M., ... & Ye, J. (2024). INSIDE: LLMs' Internal States Retain the Power of Hallucination Detection. ICLR24

Kuhn, L., Gal, Y., & Farquhar, S. (2023). Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation. ICLR23

Aichberger, L., Schweighofer, K., Ielanskyi, M., & Hochreiter, S. (2024). Semantically Diverse Language Generation for Uncertainty Estimation in Language Models. arXiv

Farquhar, S., Kossen, J., Kuhn, L., & Gal, Y. (2024). Detecting hallucinations in large language models using semantic entropy. Nature

Bakman, Y. F., Yaldiz, D. N., Buyukates, B., Tao, C., Dimitriadis, D., & Avestimehr, S. (2024). MARS: Meaning-Aware Response Scoring for Uncertainty Estimation in Generative LLMs. arXiv

Duan, J., Cheng, H., Wang, S., Wang, C., Zavalny, A., Xu, R., ... & Xu, K. (2023). Shifting attention to relevance: Towards the uncertainty estimation of large language models. ACL

### Soundness
1

### Presentation
1

### Contribution
2
