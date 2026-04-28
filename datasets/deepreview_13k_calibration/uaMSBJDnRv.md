# Unintentional Unalignment: Likelihood Displacement in Direct Preference Optimization

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
\vspace{-1.25mm}
Direct Preference Optimization (DPO) and its variants are increasingly used for aligning language models with human preferences. 
Although these methods are designed to teach a model to generate preferred responses more frequently relative to dispreferred responses, prior work has observed that the likelihood of preferred responses often decreases during training.
The current work sheds light on the causes and implications of this counter-intuitive phenomenon, which we term \emph{likelihood displacement}.
We demonstrate that likelihood displacement can be \emph{catastrophic}, shifting probability mass from preferred responses to responses with an opposite meaning.
As a simple example, training a model to prefer \texttt{No} over \texttt{Never} can sharply increase the probability of \texttt{Yes}.
Moreover, when aligning the model to refuse unsafe prompts, we show that such displacement can \emph{unintentionally lead to unalignment}, by shifting probability mass from preferred refusal responses to harmful responses (\eg, reducing the refusal rate of Llama-3-8B-Instruct from 74.4\% to 33.4\%).
We theoretically characterize that likelihood displacement is driven by preferences that induce similar embeddings, as measured by a \emph{centered hidden embedding similarity (CHES)} score.
Empirically, the CHES score enables identifying which training samples contribute most to likelihood displacement in a given dataset.
Filtering out these samples effectively mitigated unintentional unalignment in our experiments.
More broadly, our results highlight the importance of curating data with sufficiently distinct preferences, for which we believe the CHES score may prove valuable.
}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper discusses a curious and interesting phenomenon - likelihood displacement in LLMs where alignment methods actually can lead the model to be unaligned by placing much higher probability on semantically different outputs (thereby reducing the probability from preferred responses). The authors identify that likelihood displacement can be quite catastrophic, and attribute this to the geometry of the token embeddings. They introduce a metric, the Centered Hidden Embedding Similarity (CHES) score, to identify training samples that contribute most to likelihood displacement and show that filtering out high-CHES samples mitigates unalignment issues effectively.

### Strengths
The authors have provided quite valuable insights into the phenomenon of likelihood displacement. They have provided detailed theoretical analysis to justify their claims. I found the connection with the difference of the token unembeddings (corresponding to preferred and non-preferred outputs) quite interesting, and although it's not too hard to derive, it's good that someone pointed this out. I do this this paper will  generate quite a bit of discussion and follow up work.

### Weaknesses
I don't think there is any major weakness.

### Questions
N/A

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates a phenomenon of “likelihood displacement” in DPO, i.e. the probability of preferred responses decreases instead of increasing, sometimes causing models to produce semantically opposite responses unintentionally. Based on the analysis, the authors propose a CHES score to identify training samples likely to cause likelihood displacement. The authors also empirically show that filtering out these samples effectively mitigates the unalignment.

### Strengths
1.	The paper theoretically develops a theoretical understanding of how and why likelihood displacement occurs and validates this with experiments across multiple models.

2.	CHES score provides a useful guidance to pick useful data to further enhance model performance, and potentially serves as a tool to curate preference dataset.

### Weaknesses
1. The scope of the experimental scenarios is a concern. While the experiments include several models and datasets, the scenarios are somewhat limited. They primarily focus on refusal responses, which are single-token. To verify the robustness of the findings, other scenarios, including multi-token responses and diverse types of responses, are encouraged to test out.

2. From the experiment result in Section 6, it looks like using CHES for data filtering improves the performance a lot on top of DPO. It would be great if the authors can further explore the effect of CHES filtering on more realistic tasks like finetuning on ultrafeedback dataset with models tested in the paper, compared with other baselines.

### Questions
1.	How does likelihood displacement evolve over longer training periods? Does it diminish or intensify as the training goes?

2.	Is there any recommended threshold for CHES filtering?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work explores the causes and effects of a phenomenon in direct preference learning, referred to by the authors as likelihood displacement, where the probability of preferred responses decreases. This counterintuitive occurrence is attributed to the similarity of preference embedding, quantified using a centered hidden embedding similarity (CHES) score. This score is valuable for data selection, helping to avoid unintentional unalignment, a catastrophic phenomenon identified by the paper. The reviewer finds the paper clearly written, offering valuable insights into a commonly recognized but not well-understood issue in DPO training, with interesting and solid theoretical analysis backing the results under a simplified but reasonable mathematical setup.

### Strengths
1. The paper is quite clearly written, and the theoretical results for analyzing likelihood displacement are sound and well presented.
2. The paper also analyzes the variants of direct preference learning algorithms that explicitly adds SFT loss on preferred responses as regularization and shows that is can mitigate likelihood displacement.
3. The experiments demonstrate the power of the CHES score in identifying samples that lead to decreasing probability of preferred responses and its utility in data filtering to prevent unintentional unalignment.

### Weaknesses
1. The unconstrained feature model is not realistic and an oversimplification. But the reviewer does appreciate the attempt towards analyzing the phenomenon of likelihood displacement from a rigorous theoretical perspective.
2. The theoretical results are restricted in analyzing the local change of log probability of preferred labels, while a comprehend analysis of the entire dynamic of the changes in the log probabilities is unknown, even for the simplified single data and single output token case. Such analysis can give better characterization of whether the log preferred response probability goes up or down after direct preference learning.

### Questions
1. In Section 4.2.1., Line 297, why the orthogonal component of $\mathbf{W}\_{\mathbf{y}^+} - \mathbf{W}\_{\mathbf{y}^-}$ w.r.t. $\mathbf{W}\_{\mathbf{y}^+}$ is $\mathbf{W}\_{\mathbf{y}^-}$? It seems that from Theorem 1 if the likelihood displacement happens (in this specific setting of single token response), the two unembeddings should be well aligned, i.e., $\langle \mathbf{W}\_{\mathbf{y}^+} , \mathbf{W}\_{\mathbf{y}^-}  \rangle$ is relatively large, and in this case the projection to the orthogonal space of $\mathbf{W}\_{\mathbf{y}^+}$ is not likely to be introduced by $\mathbf{W}\_{\mathbf{y}^-}$. Can the authors explain more about the intuition here? 
2. While the authors argue that the CHES score (Definition 2) reflects the similarity of the preferred response and the rejected response, it is a little bit vague to strictly say this from its expression because the CHES score also involves a negative term of the norm of the preferred response summed embeddings. How should one interpret such explanations made in the paper mathematically? 
3. Continued from 2., from Theorem 1, the unembedding geometry also influences the change of the log preferred response probabilities. Why does the CHES score not involve terms related to the unembedding geometry of the responses?
4. Does the unintentional unalignment also appear in RLHF algorithms (other than direct preference learning, e.g., PPO)? If so, can it also be explained by the mechanism proposed by this paper? 
5. What is the implication of the analyzed method in the domain of complex reasoning like math problem solving and code generation? Does the proposed data filtering method also help to improve the reasoning capability of the model trained?
6. Typos, Line 959: $\mathbf{W}\_{\mathbf{y}_!}$ should be $\mathbf{W}\_{\mathbf{y}_1}$

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
3

### Summary
This paper studies the problem of *unintentional unalignment* in RLHF: when aligning a model with RLHF with DPO, the opposite of the desired effect can happen. For example, when aligning Llama-3-8B, we observe a drastic reduction of the refusal rate on SORRY-Bench.

This paper suggests that this phenomenon is due to embedding similarities of undesirable and desirable properties fed to the model. As a consequence, the model can only decrease the probability of both outputs, leading to the increase probability of an alternative, potentially harfmul, output.

To mitigate this effect, the authors propose a CHES score, which allows to select only a fraction of the data when running DPO. This data selection then allows to better performance on benchmarks such as SORRY-Bench.

### Strengths
The study of RLHF is of course an important topic, as it is implemented to align LLMs, while still presenting clear flaws, such as the one of unintentional unalignement. This work proposes a nice and simple explanation for this phenomenon, which can then lead to the design of strategies that mitigate such effect.

This work presents extended experiments on the SORRY-Bench dataset, where their curated data method allows to reach strong refusal rates.

### Weaknesses
While the presentation seems to insist on the theoretical contribution of this work, I find it pretty weak. More precisely, Theorems 1 and 3 just seem to be the result of the computation of a gradient. Moreover, Theorem 3 is a bit disappointing, as it depends on some factors $\alpha_{k,k'}$ for which we don't know the sign (besides an empirical study).

As a consequence, I do not see the theoretical contribution of this work as a strong contribution, and I thus expect it to be strong on the empirical side. On the empirical side now, I find the experiments on the SORRY-Bench benchmark interesting and promising. Yet, I have the following main critique regarding this work:

**RLHF has not the sole objective of maximizing the refusal rate, but at aligning with human preferences in many different aspects**

I indeed feel that this work considers the performance of a RLHF method solely on its refusal rate. Indeed, the only experiments are done wrt this metric, but I would also like to see if the proposed algorithm does not lead to poorer performances on different benchmarks (with different objective than refusal rates), such as evol-instruct.

Indeed, if the only objective was to maximize the refusal rate, then a better, obvious algorithm should be the following one: we only consider two possible values for $y^+$ and $y^-$, given by "Acceptance" and "Refusal" and fine-tune the model with such a dataset. Presumably, I guess there is no better algorithm to optimize the "refusal rate" metric, as it is explicitly and directly optimizing this metric.
On the other hand, the CHES based method does not do that explicitly, but I suspect it is close to that in the end. So why should we not directly optimize on the refusal rate? I guess such a method could lead to poorer performances on more complex alignment tasks: as a consequence, I feel that measuring the performance of the algorithm on such tasks is also needed to validate the interest of the proposed algorithm.

### Questions
- What are the performances of the proposed algorithm on alignment benchmarks that are not about refusal rate?
- Why could we not simply directly optimize the refusal rate?

### Soundness
3

### Presentation
4

### Contribution
2
