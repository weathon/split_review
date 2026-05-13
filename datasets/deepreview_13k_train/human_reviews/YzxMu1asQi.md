# Scaling Laws for Adversarial Attacks on Language Model Activations and Tokens

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
\noindent We explore a class of adversarial attacks targeting the activations of language models. By manipulating a relatively small subset of model activations, $a$, we demonstrate the ability to control the exact prediction of a significant number (in some cases up to 1000) of subsequent tokens $t$. We empirically verify a scaling law where the maximum number of target tokens $t_\mathrm{max}$ predicted depends linearly on the number of tokens $a$ whose activations the attacker controls as $t_\mathrm{max} = \kappa a$, and find that the number of bits of control in the input space needed to control a single bit in the output space (that we call \textit{attack resistance $\chi$}) is remarkably constant between $\approx 16$ and $\approx 25$ over 2 orders of magnitude of model sizes for different language models. Compared to attacks on tokens, attacks on activations are predictably much stronger, however, we identify a surprising regularity where one bit of input steered either via activations or via tokens is able to exert control over a similar amount of output bits. This gives support for the hypothesis that adversarial attacks are a consequence of dimensionality mismatch between the input and output spaces. A practical implication of the ease of attacking language model activations instead of tokens is for multi-modal and selected retrieval models, where additional data sources are added as activations directly, sidestepping the tokenized input. This opens up a new, broad attack surface. By using language models as a controllable test-bed to study adversarial attacks, we were able to experiment with input-output dimensions that are inaccessible in computer vision, especially where the output dimension dominates.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes an adversarial attack on the activations of LLMs and studies scaling laws for the attack. The results show that by perturbing a small set of model activations, prediction tokens can be controlled. A linear scaling law between perturbed activation tokens and predicted tokens is empirically validated. This threat model is claimed to practical in retrieval tasks and in certain multi-modal models.

### Strengths
The scaling law study for adversarial attacks on language model activations allows exploration in input-output regimes much larger than previously studied computer vision models.

### Weaknesses
As mentioned in Line 268, the attacks used are close to iterative gradient attacks or FGSM which were proposed early in the computer vision literature. Is it comprehensive enough to do this study limited to these attack models. Also, is it common to keep the perturbations unbounded for LLM attacks?

It is unclear if there is any supporting evidence in literature for "The core hypothesis is that the ability to carry a successful adversarial attack depends on the ratio between the dimensions of the input and output spaces."

Typos (Line 262, 267 ,315) the reference to Algorithms are incorrect.

(Line 499) It's incorrect use of the Big-O notation. O(100) is equivalent to any O(k) where k is a constant. So, it's best to rephrase this line.

### Questions
1. Is there any supporting evidence in literature for "The core hypothesis is that the ability to carry a successful adversarial attack depends on the ratio between the dimensions of the input and output spaces."

2. Typos (Line 262, 267 ,315) the reference to Algorithms are incorrect.

3. (Line 499) It's incorrect use of the Big-O notation. O(100) is equivalent to any O(k) where k is a constant. So, it's best to rephrase this line.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the technique of adversarial attacking the activation value of LLM. This work explains the LLM's vulnerability and finds that attacks satisfy scaling law.

### Strengths
The problems studied are important because LLM has been applied to our life. The proposed attack method can achieve good results and shows some inherent characteristics of LLM itself.

### Weaknesses
The practicality of the proposed scheme is questionable, and whether this attack scheme can be implemented in reality needs further consideration.

The utility of LLM activation values to attacks needs to be fully explained. Only two works discussing modifying activation values are presented in the introduction of this paper. And the work of the retrieval and multimodality seems to be to concatenate activations from different inputs, rather than to add a certain perturbation of activations, as is the case against attacks.

Is the attacker a user? How can an attacker inject generated adversarial perturbations into benign user-generated activation values?

Does an attacker need to access the entire LLM model to calculate adversarial perturbations? The LLM model is usually provided to the user in the form of an API, and the attacker cannot obtain the model weights.

### Questions
1. The utility of LLM activation values to attacks needs to be fully explained. Only two works discussing modifying activation values are presented in the introduction of this paper. And the work of the retrieval and multimodality seems to be to concatenate activations from different inputs, rather than to add a certain perturbation of activations, as is the case against attacks.

2. Is the attacker a user? How can an attacker inject generated adversarial perturbations into benign user-generated activation values?

3. Does an attacker need to access the entire LLM model to calculate adversarial perturbations? The LLM model is usually provided to the user in the form of an API, and the attacker cannot obtain the model weights.

### Soundness
2

### Presentation
2

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
The paper considered activation-level rather than token-level adversarial attacks on LLMs and derives scaling laws between the number of output tokens an attacker can affect vs the number of input activations they can control. The paper also explores token-level substitution adversarial attacks in comparison to their novel approach.

The paper justifies the practicality of their activation-level attacks by referencing retrieval and multi-modal models. It concludes by drawing general implications of this work for the adversarial ML community, namely presenting language models as a more flexible environment for exploring the theory of adversarial attacks compared to vision models.

### Strengths
Originality:
 * As far as I can tell this is the first paper to take an in-depth look at activation-level adversarial attacks
 * The comparison of token vs activation level attacks isn’t surprising due to the significantly higher level of granular control you can exhibit on the activation level but good to have it quantified

Quality:
 * Clear writing style, thought process and hypothesis clearly stated and explained

Clarity:
 * Core idea and experiments clearly presented and explained.

Significance:
 * Strong practical justification of the real-world applicability of the research through reference to retrieval and multi-modal setups.
 * Presents a compelling case for using LLMs and activation-level attacks as a test bed

### Weaknesses
 * Presentation and explanation of the theory of the attack strength could be better – it’s currently a large hard-to-read paragraph while references are repeatedly made to the empirical vs theoretical scaling laws. E.g., breaking down the working of the final equation. The derivation lacks sufficient detail, making it difficult to fully grasp the relationship between the controlled activations and the resulting output token manipulation. The paper would benefit from a step-by-step explanation of how the final equation is derived, including the assumptions made and the limitations of the theoretical model. Furthermore, the connection between the theoretical scaling laws and the empirical results should be made more explicit, with a discussion of any discrepancies and their potential causes.
* The narrative of the paper feels a bit non-linear – I had to skip ahead or read back multiple times to reference material presented in the paper to bits where it was relevant again. For example in L153 the significance of the log2 value is only appreciated after reading the scaling laws subsection. The paper jumps between different aspects of the research without providing clear transitions or signposting. This makes it challenging to follow the authors' line of reasoning and to understand the significance of each finding in the broader context of the paper. The lack of a clear narrative flow also makes it difficult to retain the information presented in the paper.
* Some of the more vague speculative statements such L204 “(although adversarial training probably changes it)” should probably be avoided and left to a “future research” section. Ditto L222-223 regarding the effective dimensionality of the embedding – this specifically would be very interesting to explore separately. These statements, while potentially interesting, detract from the main focus of the paper and introduce unnecessary speculation. The lack of concrete evidence to support these claims makes them less convincing and weakens the overall argument of the paper. It would be more appropriate to present these ideas as potential avenues for future research, rather than as conclusions drawn from the current study.
* Some of the plots should be included as PDFs rather than images for fidelity’s sake. E.g. Figure 1(b,e), Figure 3, Figure 5. This is important as the graphs are dense and small for an A4 page. I would also recommend increasing the font size to improve readability. The current image format results in a loss of detail, making it difficult to accurately interpret the data presented in the figures. The small font sizes further exacerbate this issue, making it challenging for the reader to extract the necessary information from the plots. Using vector graphics (PDFs) would ensure that the figures are displayed with maximum clarity and detail, regardless of the zoom level.
* This is a side note but the appendix appears to be incomplete with sections C, D, E appearing empty

### Questions
* Is χ related to concepts such as generalised degrees of freedom (https://auai.org/uai2016/proceedings/papers/257.pdf Gao and Jojic 2016) or effective dimensionality (https://arxiv.org/abs/2003.02139 Maddox et al 2020)? It feels like a similar concept
* Worth exploring how adversarial training affects χ 
* Would make for an interesting separate research paper to explore the effective dimensionality of the activation dimensions and maybe how that could be used for compression. This is in reference to L222-223.

### Soundness
3

### Presentation
2

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
The paper proposes a hypothesis: there is a "scaling law" between number of input tokens the attacker can modify and the number of prediction tokens the model outputs.  Empirical results suggest that under certain cases, the maximum number of target tokens that can be manipulated by the attacker, depends linearly on the number of input tokens that the attacker can control.

### Strengths
+ S1: The research work is of great novelty and originality. The hypothesis proposed in the paper is interesting.

+ S2: Empirical findings can provide support to the proposed hypothesis. Such scaling law can be observed on several different language models.

### Weaknesses
Although the hypothesis is interesting, there are many details not discussed clearly which hinders the readers from a deeper understanding. 

+ W1: **Formulation and measure of $t_{max}$ lacks clarity**.  $t_{max}$ is designed to present the ideal maximum tokens that attacker can manipulate in model prediction. However, how to practically obtain this amount may be unclear. From the paper describes a random sampling strategy to obtain context tokens $S$ and target tokens $T$. It raises questions about the impact of different samples on $t_{max}$ value. How many ($S$, $T$) pairs are sampled to determine $t_{max}$? What is the distribution of $t_{max}$ across various samples? Intuitively, the length of target tokens might extend to a larger value if they are more aligned with natural language priors or they are from (repeated) training samples, such as excerpts from famous poems. For random combination of tokens in $T$ and $S$, different samples may get varied attack performance. This is very important since changes to the value of $t_{max}$ may result in the linearity of relationship no longer holds. More detailed discussion on this manner would benefit readers' understanding. 

+ W2: **Practicality of the attack is questionable**.  One notable setting in this paper is the attacker's ability to modify the activations of token feature without limit (different from the classic adversarial attack setting where the attacker needs to constrain their perturbations within a $\epsilon$-ball).  While authors provide examples involving retrieval and multi-modal models where an attacker might alter continuous feature values within the model, the feasibility of such unlimited modifications are questionable. For example, in multi-modal models, a more realistic attack surface would be the attacker altering an image within [0, 255] pixel range, rather than arbitrarily modifying image features. The impractical threat model may undermine its real-world relevance and impact of presented findings.


+ W3: Typo and broken sentence
    - a) Line 283, "probability can be seen in e.g. Figure 3a and Table 1 refers to the ..." ?

### Questions
My questions are aligned with the weakness part. 

+ Q1: Regarding W1,
  - a) Can you specify exact number of ($S$, $T$) pairs sampled for each $t_{max}$ estimation? 
  - b) Provide error bars or confidence intervals for the $t_{max}$ values to show the distribution across samples.
  - c) Include an analysis of how $t_{max}$ varies for different types of target sequences (e.g. random tokens vs natural language).
  - d) Discuss how the variability in tmax estimates impacts the linearity of the scaling relationship.


+ Q2: Regarding W2,
  - a) Can you provide a more detailed analysis of realistic constraints on activation modifications in retrieval and multi-modal settings?
  - b) Can you conduct experiments with bounded perturbations (e.g. within an ε-ball) to see how this affects the scaling law.
  - c) Discuss more explicitly the limitations of your unconstrained attack model and its implications for real-world applicability.

### Soundness
3

### Presentation
2

### Contribution
3
