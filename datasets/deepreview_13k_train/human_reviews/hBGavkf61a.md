# Diffusion Bridge AutoEncoders for Unsupervised Representation Learning

- Decision: Accept
- Scores: 8, 8, 8, 5

## Abstract
Diffusion-based representation learning has achieved substantial attention due to its promising capabilities in latent representation and sample generation. Recent studies have employed an auxiliary encoder to identify a corresponding representation from a sample and to adjust the dimensionality of a latent variable $\rvz$. Meanwhile, this auxiliary structure invokes \textit{information split problem} because the diffusion and the auxiliary encoder would divide the information from the sample into two representations for each model. Particularly, the information modeled by the diffusion becomes over-regularized because of the static prior distribution on $\rvx_T$. %unidentifiable
To address this problem, we introduce Diffusion Bridge AuteEncoders (DBAE), which enable $\rvz$-dependent endpoint $\rvx_T$ inference through a feed-forward architecture. This structure creates an information bottleneck at $\rvz$, so $\rvx_T$ becomes dependent on $\rvz$ in its generation. This results in two consequences: 1) $\rvz$ holds the full information of samples, and 2) $\rvx_T$ becomes a learnable distribution, not static any further. 
We propose an objective function for DBAE to enable both reconstruction and generative modeling, with their theoretical justification. Empirical evidence supports the effectiveness of the intended design in DBAE, which notably enhances downstream inference quality, reconstruction, and disentanglement. Additionally, DBAE generates high-fidelity samples in the unconditional generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper identifies The paper identifies a problem in diffusion-based representation learning models with auxiliary (lower dimensional) latent variables, which the authors call the "information split problem".
The identified problem is that such models rely on both the auxiliary latents $z$ and the diffusion endpoint $x_T$ when reconstructing (or unconditionally generating) data.
Thus, even a well-trained model (i.e., a model that can reconstruct data well) may not encode all relevant features of a given data point $x_0$ in $z$ and instead rely also on $x_T$ when reconstructing it.
This makes $z$ less useful as a representation of $x_0$ in downstream tasks (e.g., classification, clustering).

The paper proposes to resolve this issue by turning $z$ into an information bottleneck, thus ensuring that $x_T$ is conditionally independent from $x_0$ given $z$ (i.e., $x_T$ cannot contain any additional information about $x_0$ that is not already encoded in $z$).
The paper discusses and empirically evaluates training objectives of their proposed architecture for representation learning, reconstruction, and unconditional generation.

### Strengths
The paper addresses an important issue in representation learning with diffusion models.
The proposed solution appears theoretically sound and empirically convincing to me, but I have to admit that I am not an expert on the relevant literature regarding other solutions to the discussed issue (if any), nor on state-of-the-art empirical performance, so I will yield to the judgment of the other reviewers in this regard.

The paper is remarkably well organized.
Despite addressing a rather complicated problem in a domain that requires a lot of prior knowledge, the paper manages to be self-contained and discusses all relevant background in a brief yet (as far as I can tell) complete way.
The addressed problem is introduced in a didactic way (first with examples, then gradually more formal), and its proposed solution is well motivated.

### Weaknesses
I am not an expert on diffusion models with auxiliary encoders, so I cannot judge the novelty of the proposed method or the choice of baselines in the empirical evaluation.

I only identified minor weaknesses (although I strongly recommend addressing at least the last point below as it should be relatively easy to fix and would make the paper much more accessible).

I did not understand the significance of the information split problem in unconditional generation (Section 4.4.2).
I appreciate that the discussion of the objective function (Section 4.4) distinguishes between different use cases of diffusion models.
And I can see that the described information split problem can be an issue for representation learning.
But if all we care about are good unconditional samples, then why does it matter whether $x_T$ may contain some information that is not contained in $z$?
We would sample $x_T$ anyway.
Yet, empirically, it seems like the proposed DBAE+AE model outperforms the baselines even for unconditional generation.

Further, as a minor point, Eq. 9 seems suspicious to me.
While I understand how a bound of this form would exist in general, in the specific instance both $p_\theta^\text{ODE}(x_0 | z, x_T)$ and $p_\theta^\text{ODE}(x_T |z_0, z)$ are delta-distributions unless I am mistaken, so the log-density of the former does not exist, and I would expect the KL-divergence term that involves the latter to be infinite.
I presume that the "two infinities cancel" in some sense, but maybe the equation could be rewritten in a way that doesn't rely on "cancellation of infinities".

Apart from this, my only criticism concerns the large number of grammatical errors, which made the paper quite a bit more difficult to read for me than necessary.
This is a shame because it diminishes the otherwise excellent presentation.
I know that being overly pedantic on grammar in scientific papers can impose cultural bias, but I am fairly certain that most of the errors could be caught by automatic tools.
And while many errors are somewhat trivial (singular/plural or missing/superfluous/wrong articles), some sentences were right-out unintelligible to me and I had to pause reading and infer the intended meaning from context.
Some examples include (there are more): lines 132-133, lines 160-162 (two separate sentences that were probably meant as one, but this isn't immediately apparent due to remaining grammar issues even when joining them), and lines 287-288 (missing verb; I actually can't infer the intended meaning here).
I strongly recommend running the entire paper through a grammar checker, or asking an LLM to detect possible grammar issues in each paragraph.
It would make this otherwise great work more accessible to a broad (international) audience.

### Questions
What is the significance of the information split problem in unconditional generation (see "Weaknesses")?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes Diffusion Bridge AutoEncoders to create latent variable-dependent endpoint embeddings, resolving the information split problem due to the auxiliary encoder and fixed and inflexible dimension problems in diffusion-based models. 

With theoretical guarantees, the method outperforms the SOTA methods on various datasets and settings.

### Strengths
Quality and clarity: the paper is well-written and the idea is motivated and easy to follow. 

Originality: the paper aims to solve the so-called information-split problem in the field. The effectiveness of the proposed method is well-supported by theorems and comprehensive experiments. 

The theorems indicate the proposed loss can indeed increase the mutual information between the input images and the latent variable. Moreover, the generated data distribution is guaranteed to be close to the input data distribution by the proposed loss.

The experiments show substantial improvement in the proposed DBAE method in terms of downstream tasks, reconstruction, disentanglement, and generation. Furthermore, the inference speed is also superior obviously.

### Weaknesses
1. It is unclear how the loss makes the endpoint dependent on the latent variable. The theorems only show the relationship between the input data and the latent variable instead, which is not aligned with the claim.

2. The intuition is missing in Section 4.1. For example, why the new forward SDE is defined as in Eq. 10? Providing more intuition would help readers to appreciate the forward process.

### Questions
1. Could you provide more intuition behind Eq.10?

2. The paper proposes the AutoEncoder structure for the Diffusion-based representation learning methods. Would it also be interesting to appreciate the work from a (Variational)AE perspective? Will this work provide insights to both sides as a bridge in the middle?

3. Lastly, why and when the split of information will be problematic? For example, in the generation step, the information will be combined from both the latent variable and the endpoints. Thus, is it really necessary to have the information stored or learned in a single representation?

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
3

### Summary
This paper proposes a new Diffusion VAE model in order to combine the latent representation power of VAE and the generation power of Diffusion models. In previous Diffusion VAEs, the latent variable $z$ and $x_T$ are encoded separately from the data $x_0$. The latent variable is concatenated during the denoising process. However, the starting point $x_T$ is not dependent on $z$. The authors call this problem an information split, which can cause unfaithful reconstruction from $z$ and a large gap of mutual information. Motivated by this, the authors introduce another decoder from $z$ to $x_T$. Therefore, $x_T$ can obtain information from the original data. This dependence reduces the mutual information gap, and enhances the representation learning performance. The overall model appears to be a concatenation of VAE and the diffusion process. The authors conduct comprehensive experiments to show advantages in latent variable learning and generation.

### Strengths
1. Combining VAE with diffusion is of practical interest. The motivation and solution seem reasonable to me. The authors also provide some theoretical justifications of the model and objective functions.

2. There are thorough experiments to demonstrate the usefulness and performance of the proposed model.

### Weaknesses
1. In the diffusion bridge Eq. (5), the input is transformed into a fixed target. However, in the proposed model, the target $x_T$ is random due to the randomness of the VAE. Does this affect the theory? Specifically, the derivation of the diffusion bridge relies on a deterministic target, and it's unclear how the stochasticity introduced by the VAE's latent variable affects the validity of the derived equations. The paper should provide a more rigorous justification for applying the diffusion bridge framework with a stochastic target.

2. In Section 4.4, the authors present objective functions for reconstruction and generation tasks. In experiments, did the authors optimize different objectives and use different models for different tasks? Can we obtain both reconstruction and generation abilities using the same model? It's not clear whether the model is trained end-to-end for both tasks or if separate training procedures and potentially different model parameters are used. This distinction is crucial for understanding the practical applicability of the proposed method. The paper should clarify the training procedure and the model architecture used for each task.

3. I am wondering whether the training is difficult compared to without the AE part. Is there a trade-off between the expressive power of the AE and diffusion model? The paper lacks a discussion on the potential challenges introduced by the addition of the VAE component, such as increased training complexity, sensitivity to hyperparameter tuning, and potential for mode collapse in the latent space. It would be beneficial to see an analysis of the training stability and the impact of the AE's capacity on the overall performance.

### Questions
See above

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
This paper introduces the Diffusion Bridge AutoEncoders (DBAE) framework to address the "information split problem" in diffusion-based autoencoding models for unsupervised representation learning. The authors argue that in conventional latent-variable-augmented diffusion models, the information in data $x_0$ is split between two latent variables--$z$, obtained from an auxiliary encoder, and $x_T$, the endpoint of the diffusion process. This split hinders effective encoding, especially for downstream tasks such as reconstruction. DBAE proposes a solution to remedy this by creating a dependency of $x_T$ on $z$, allowing $z$ to serve as a comprehensive information bottleneck and improving representation quality. Specifically, the authors propose the process to encode $x_0$ into $z$, decode $z$ into $x_T$, and then bridge $x_0$ and $x_T$ to define a diffusion process. The authors provide empirical evidence supporting DBAE’s improvements in representation quality, reconstruction, and downstream tasks, suggesting it as a promising model for generative and reconstruction purposes.

### Strengths
This paper addresses a key challenge in latent-variable generative models, particularly in diffusion probabilistic models (DPMs) that are augmented with an auxiliary encoded latent variable $z$, which the authors refer to as the "information split problem." The authors clearly illustrate how the information split between $z$ and $x_T$ diminishes the quality of latent representations for high-fidelity tasks. To overcome this issue, they propose a principled framework that integrates autoencoders with diffusion models by (1) encoding $x_0$ to define the latent endpoint $x_T$ of the diffusion process, and (2) connecting these two points utilizing Doob’s $h$-transform. This approach combines the strengths of autoencoders—such as dimensionality reduction and efficient encoding/decoding—with the rich generative capabilities of diffusion models. Experimental results demonstrate that DBAE outperforms existing models across various benchmarks, underscoring its effectiveness in tasks like generation, reconstruction, and attribute manipulation. The paper also discusses potential extensions of DBAE to various downstream applications, highlighting its adaptability and potential for broader impact.

### Weaknesses
Despite its strengths, I think the paper’s impact is significantly diminished by its presentation. Below, I outline major concerns with suggestions for improvement.

**Clarifying Motivation and Significance in the Introduction:**
The Introduction lacks a clear articulation of why the “information split problem” is critical to address. This issue is specific to a subset of diffusion probabilistic models (DPMs) that are augmented by an auxiliary encoded latent variable $z$. For readers to appreciate the significance of this issue, it would help to emphasize the relevance of these models, which combine strengths from both VAEs and DPMs. While the first two paragraphs provide an overview of latent-variable generative modeling, the current description introduces these models merely as proposed approaches rather than as leading techniques in the field. Highlighting their role as state-of-the-art or best-performing models would better contextualize the importance of tackling their limitations. Additionally, the Introduction could clarify why the information split problem is particularly relevant for tasks requiring accurate reconstruction of the original data, $x_0$. The authors might adapt statements like those in Lines 285–286—“For downstream inference, attribute manipulation, and interpolation, the model requires reconstruction capability”—to illustrate the utility of generative modeling and explain the advantages of integrating VAE and DPM functionalities. Establishing these goals clearly would help readers understand how the information split issue primarily affects reconstruction and how DBAE addresses this challenge.

**Improving Precision in Terminology and Expression:**
Several terms and expressions in the paper would benefit from clearer definitions and consistent use. For instance, in Line 49, “inference of $x_T$” may be ambiguous; specifying this as “estimating the latent variable $x_T$ conditioned on $x_0$” would clarify the intent. Similarly, the phrase “latent variable inference,” which appears in Section 4.1, could be made more precise by using “estimating $x_T$ conditioned on $z$” or “encoding $x_0$ into $x_T$,” depending on the context. Certain expressions, like "$D_{KL}(q_{\theta}^{\textrm{ODE}}||p_{\textrm{prior}})$ explains the information split problem” (Lines 196–197), are unclear; it would help to specify whether the KL divergence term’s presence illustrates or quantifies this problem. Ensuring precise and consistent terminology throughout would enhance readability and help avoid potential confusion (see “Questions” for further specific comments).

**Providing Precise Description of Methodology/Tasks in Sections 4 & 5:**
- *Methodology in Section 4:* The presentation of the proposed methodology in Section 4 is complex and challenging to follow. A concise pseudocode or boxed algorithm format summarizing DBAE’s key steps, including training and inference procedures, would streamline comprehension. Providing a pseudocode outline for DBAE’s main processes—inferring $z$ from $x_0$, subsequently inferring $x_T$ from $z$, and bridging $x_0$ and $x_T$ using Doob’s $h$-transform—would help organize the workflow and provide readers with a structured overview before diving into the details.
-  *Experimental Tasks in Section 5:* Section 5 could also benefit from a more systematic presentation of the six experimental tasks under investigation. Providing a precise, mathematical description of each task would make it easier for readers to interpret DBAE’s advantages across different contexts. For example, the description of Interpolation problem in Lines 474 - 476 can be a good starting point -- presenting all tasks in a similar manner would help readers understand the desiderata and challenges in each tasks as well as DBAE’s benefits across varied applications in a more structured way.

### Questions
Line 46: The phrase “and the endpoint $x_T$” may be unclear. Would it be more precise to revise this to “to the endpoint $x_T$” to clarify the relationship between $z$ and $x_T$?

Line 49: The term “inference of $x_T$” might be ambiguous for some readers. Could this be rephrased or annotated as “estimating $x_T$ conditioned on $x_0$” or “encoding $x_0$ into $x_T$”?

Lines 75–80: The third paragraph of the Introduction could benefit from additional clarity. The challenges described here seem to presuppose the goal of compressing $x_0$ into latent variables ($z$ and $x_T$) for reconstruction, but this goal is not explicitly stated, which could cause confusion. For example, readers focused on new sample generation might not understand why the information split issue affects reconstruction. Would the authors consider clarifying this context and explaining why reconstruction is a primary focus?

Line 99: Consider capitalizing “eq.” to “Eq.” when referencing specific equations. Also, while referencing equations before presenting them can add context, it is uncommon and might disrupt the logical flow. Would it be more effective to present equations first, then reference them?

Lines 160–161: It might be helpful to provide the full names of “VE” and “VP” (at least in a footnote), rather than only using acronyms, to support readers who may be unfamiliar with these terms.

Lines 196–197: For clarity and parallelism, consider specifying that $D_{KL}(q_{\theta}^{\textrm{ODE}}, p_{\textrm{prior}})$ represents the KL divergence between $q_{\theta}^{\textrm{ODE}}$ and $p_{\textrm{prior}}$. The phrase “$D_{KL}$ explains the information split problem” is also somewhat ambiguous. Could the authors clarify whether the KL divergence term’s presence illustrates or quantifies the problem? Additional context could improve reader understanding.

Lines 203–204: Since the references here were cited just two paragraphs above, the authors may want to omit them to save space.

Line 213: The title of Section 4.1, “latent variable inference,” may be unclear—does it refer to $z$, $x_T$, or both? Clarifying whether the authors mean both variables, and if so, how they relate, would improve clarity.

Lines 214–215: The nature of the encoder and decoder is not clearly defined. For instance, is $\text{Enc}{\phi}$ deterministic or stochastic? If it is deterministic, how does it define the conditional probability $q{\phi}$? Clarifying this would assist readers in understanding the model structure.

Section 4: A concise pseudocode format summarizing the main DBAE algorithm, including training and inference procedures, would be helpful. Consider adding boxed pseudocode for core processes, such as (1) inferring latent variables for reconstruction or sample generation, and (2) training the encoder and decoder. This structured overview could improve comprehension before diving into the details.

Section 4.1: It would be helpful if the authors could confirm the proposed procedure: (1) infer $z$ from $x_0$, (2) infer $x_T$ from $z$, and (3) use Doob’s $h$-transform via Eq. (10) to bridge $x_0$ and $x_T$ and determine the distribution of intermediate $x_t$ values. Additionally, it is unclear if the encoder $q_{\phi}$ and decoder $q_{\psi}$ require training. Could the authors clarify this?

Line 285–286: The statement “For downstream inference, attribute manipulation, and interpolation, the model requires reconstruction capability” could be introduced earlier in the Introduction to help illustrate the utility of generative modeling and contextualize the information split problem. Would the authors consider adding this as a motivation for addressing the information split issue?

Line 317 (Theorem 1): The term “linear SDE” appears without prior explanation. Would the authors consider providing a brief definition?

Line 331: Consider removing “the” before “Section 4.4.1” for grammatical clarity.

Line 342: Replacing “optimize” with “minimize” could provide greater clarity regarding the objective.

Lines 354–355: Essential experimental details should ideally appear in the main text, rather than directing readers to the Appendix. This would allow readers to understand the experimental setup, including encoder and model architecture choices, without needing to consult additional sections. Would the authors consider including these details directly?

Section 5: Could the authors provide a concise, mathematically rigorous description of each of the six experimental tasks to clearly communicate the goals, challenges, and benefits of DBAE? For example, describing the interpolation task in mathematically precise terms, as in Lines 474–476, could serve as a model for presenting all tasks consistently.

### Soundness
2

### Presentation
3

### Contribution
2
