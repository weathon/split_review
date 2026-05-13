# Code diffusion models are continuous human noise operators

- Decision: Reject
- Scores: 5, 6, 8, 5

## Abstract
Diffusion for code generates code by iteratively removing noise from the latent representation of a code snippet.
During later steps of the diffusion process, when the code snippet has almost converged, these edits resemble last-mile repairs applied to broken or incomplete code. We evaluate the extent to which these errors are similar to those that humans are faced with and the capability of these models to perform last-mile repair. Our insight has two applications with significant impact for code repair. First, we can leverage the diffusion model for last-mile repair by adding noise to a broken code snippet and resuming the diffusion process. Second, we can leverage the diffusion model to generate an arbitrary amount of training data for other last-mile repair approaches (that are computationally more efficient) by sampling an intermediate program (input) and the final program (output) from the diffusion process. We perform experiments to evaluate both applications, as well as analyze trends in the evolution of representation through the diffusion pipeline providing insights on the reasoning observed.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors explore the potential of diffusion models in code generation, focusing on the iterative process of removing noise from the latent representation of a code snippet. As the diffusion process approaches convergence, the resulting edits resemble "last-mile repairs" applied to broken or incomplete code. This study evaluates the similarities between errors encountered by these models and those faced by human developers, assessing the models' capabilities in performing last-mile repairs. The authors propose two impactful applications: first, leveraging the diffusion model for last-mile repair by adding noise to a broken code snippet and continuing the diffusion process; second, utilizing the model to generate an arbitrary amount of training data for other last-mile repair methods, which are computationally more efficient, by sampling intermediate and final program states from the diffusion pipeline. Experiments are conducted to evaluate both applications, alongside an analysis of trends in representation evolution throughout the diffusion process, offering valuable insights into the underlying reasoning.

### Strengths
+ Novel idea.

### Weaknesses
 - Focus on Program Repair.
- Speed of Diffusion Models.
- Lack of Baselines.
- Closed Source.

### Questions
The authors present an innovative approach by combining diffusion models with program repair, highlighting the unique potential of this technique in enhancing code generation and error correction.

I have four concerns.

1. Focus on Program Repair. 

The authors claim that their exploration has two main implications: using the diffusion model for direct code repair and generating training data for specialized approaches. However, the latter application is evaluated exclusively in the context of program repair. This narrow focus raises questions about the broader applicability of their findings, especially given that the paper is titled "CODE DIFFUSION MODELS ARE CONTINUOUS HUMAN NOISE OPERATORS." It would benefit the authors to emphasize the program repair aspect more clearly and consider the implications of their work beyond this specific domain.

2. Speed of Diffusion Models. 

The authors should address the fact that diffusion models tend to be slower than other program repair approaches. A comparative analysis of the speed and efficiency of their method versus existing techniques (e.g., the most similar model without diffusion or just remove the diffusion of your approach) would provide valuable context for evaluating its practicality. 

3. Lack of Baselines. 

The paper does not adequately consider baseline models to demonstrate the effectiveness of the diffusion approach. Including comparisons with established methods (e.g., the baselines used in "https://dl.acm.org/doi/pdf/10.1145/3650212.3680323") or the baselines of the original model in Table1 would strengthen the argument for the proposed model's advantages and validate its performance claims.

4. Closed Source.

 The closed-source nature of the implementation may limit the reproducibility of results and the ability for the community to build upon this work.

### Soundness
2

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
4

### Summary
This paper explores using an unconditional diffusion model for last-mile code repair under two different settings: (1) as a training technique to directly train code repair models and (2) as a training data technique to generate synthetic code repair examples. The authors evaluate their approach on benchmarks in the domains of Excel, PowerShell, and Python using various denoiser and decoder architectures. Their experiments show notable execution and sketch match performance on the Excel and Python benchmarks.

### Strengths
**Novel Application**: The paper applies the diffusion model—a technique initially popularized in continuous data like images—to a novel domain: code repair. The approach demonstrates the potential to adapt diffusion models for the discrete and syntactic requirements of code.

**Experimental Coverage**: The experiments are carried out across multiple programming languages and data types (Excel, PowerShell, Python), providing broad validation of the technique.

### Weaknesses
 **Limited Significance of Performance Gains**: For some evaluation scenarios, such as synthetic data generation, the performance gains achieved using the diffusion-generated data appear to be only marginal. Given that the paper is presenting a new method, it would help to provide a more compelling differentiation from existing techniques. Specifically, the claim that a small model like t5-small (60M parameters) outperforms much larger models like phi-3.5-mini (3.8B) and Mistral 7B when fine-tuned on the same synthetic data is highly counterintuitive. A model of Mistral 7B’s scale should, in principle, leverage the same data far more effectively due to its capacity and generalization abilities. This discrepancy raises concerns about either the quality of the generated data or the experimental setup. 

**Incomplete Explanation on GPT-4o Prompting**: The authors do not provide adequate details on how GPT-4o was prompted for the evaluation. As performance in tasks like code repair can vary significantly depending on prompt quality, use of chain-of-thought reasoning, etc., it would be beneficial to have a complete description of the prompt structure either in the main text or in an appendix. Furthermore, the restriction of GPT-4o to basic syntactic errors seems like an artificial limitation, given that larger models are naturally better suited for generating diverse and nuanced errors that mimic human mistakes. This choice undercuts the potential of GPT-4o to generate more complex errors, which would make for richer training data. 

**Unexplored Trade-Offs**: The paper removes the natural language instruction component from the CodeFusion model, turning it into an unconditional diffusion model. However, the trade-offs involved in this design choice are not sufficiently explored. For example, one could imagine letting a large model such as GPT-4o generate an instruction describing the bug and then perform conditional diffusion on top. The revised explanation—that the model succeeds when buggy code aligns with reverse diffusion patterns—is significantly different from the original claim in the paper that the diffusion process mirrors human debugging behavior. If this adjustment represents a core shift in the narrative, the paper’s title and framing should also reflect this change to avoid misrepresenting the scope or contributions.

### Questions
* What are the Y-axes representing in Figure 6? Providing this information will help in interpreting the trends depicted there.

* The authors claim that the diffusion process mirrors human debugging behavior. However, there are no concrete qualitative examples supporting this. Could the authors include additional examples (perhaps in the appendix) showing the sampled intermediate programs from the diffusion process?

* My understanding is that the diffusion is carried out in the latent space of N embedding vectors, where N is the number of tokens in the input program, and the decoder then takes in these denoised N vectors and generates M new tokens for the decoded program, where M is not necessarily same as N. Is this correct? If so, could the authors update the mathematical formulation and Figure 2 to make this clearer to the reader?

* It would be helpful to more explicitly differentiate this work from CodeFusion (Singh et al., 2023). Including a dedicated section or paragraph that clearly states the novel contributions of this paper compared to prior work would make the paper's contributions stand out more clearly.


* Will the authors make the code and data used in this work open-source?

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
5

### Summary
This work analyzes whether (part of) the denoising process in code diffusion models mimics patterns seen in real-world program repair. It provides a range of evidence for this. It shows that diffusion models can be used to repair faulty programs by injecting noise into its embedding at the appropriate timestep in the denoising process and denoising as usual. It shows that buggy programs generated by the denoising process (before generating the correct solution) make for diverse and effective training data for program repair. And it provides a range of insights into why this works, mostly related to the way outputs of the diffusion process change over steps.

### Strengths
This work provides substantial evidence to back up an intuitive assumption, viz. that diffusion process mimic program repair to some extent. This involves reasonably significant contributions: both the method for repairing programs by introducing noise into their embeddings, and the method for generating large scale training data are noteworthy and effective. To the best of my knowledge, these are novel ideas, in that no prior work has provided empirical evidence for them. The results are well-presented and reasonably easy to follow.

### Weaknesses
The methodology, especially, could use some cleaning up. The paper uses quite a few one-letter abbreviations, some of them overloaded, and others not/inadequately explained. I list a few examples below, as well some (minor) incorrect statements.

The motivation doesn't fully connect to the results. The rationale given in the abstract and introduction is that diffusion operations may well resemble _human_ repair actions and suggests the work will investigate if denoising steps are "representative" of human repair steps. The work does not provide much proof for this conjecture. What it shows is that diffusion can repair broken programs and can be used to train program repair engines, but that is not the same as mimicking human repairs. Diffusion models learn to generate real programs from a wide variety of noisy ones. Some of those will end up resembling mistakes a human might make while others may look wildly different. At best, they train on a superset of human-like repair actions, though depending on the decoder, they may well miss some key human behaviors too. Proving that the repair actions are "human noise operators" (L74) would require a pair-wise comparison between a large dataset of human repairs and of diffusion repairs, which this work does not include. It does provide a few empirical observations of how diffusion-based repair operates (e.g. Fig. 7), but that is incomplete evidence for the premise. This doesn't subtract from the contributions of the work in terms of program repair effectiveness. I would just suggest toning down the discussion around human repair actions to note that there may be similarities but that this work does not prove that they are the same/a similar process (and in fact, that diffusion may involve many types of repairs that humans are very unlikely to encounter).

Minor Issues:

- L30: diffusion noise is not Gaussian by definition; that is just the most popular choice. Same at L92.
- L75: "changing" -> "changes"
- L148: the second occurrence of $c$ should also be $\hat{c}$
- L149: is $d$ a distance function, and if so, what distance does it measure?
- L157: $E$ is later also used to represent embeddings. Does it need to be used for the encoder if the encoder isn't used anyways?
- L182: is the inclusion of $N(...)$ here redundant, because it uses $x_0$ rather than $x_t$? The previous line already notes how $x_0$ is obtained.
- L237: nit: the sum & count formulas are incorrect; they need to sum to "A10", not "10".
- Fig. 5: the Python subplot, especially, suggests that more complex repairs require *less* noise (noise levels around 40%) than simpler ones, which contradicts the text. Does noise level refer to the step in which noise is introduced relative to the total number of steps? If so, the term is a bit confusing.
- L394: this sentence ends with comma, is it incomplete? It is unclear what 'more discrete than latent' means -- those concepts are not comparable.

### Questions
Given the drop-off between "best" and "any" in Tab. 1, what is the path to a practical approach to using diffusion for repair? Fig. 4 and 5 seem to imply that an initial guess of the distance between the broken and repaired code is often needed. It would help to know what the density is in the subplots in Fig. 5. Alternatively, do the results in Tab. 2 suggest that it is more effective to simply train auto-regressive models using diffusion-generated data, rather than to use diffusion to repair broken programs?

Please find suggestions for improving the work in the previous sections.

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
4

### Summary
This paper uses pretrained code diffusion model to fix erroneous code snippets and to obtain correct-erroneous code snippet pairs for subsequent finetuning of code models on code repair tasks. Paper reimplements CodeFusion model with additional variants and evaluates the models on code repair tasks for 3 programming languages. Next paper demonstrates the high quality of generated code pairs by comparing to using syntactic systems and gpt-4o to generate the data. Additionally this paper performs an analysis study of how diffusion model performs the code fixes.

### Strengths
The paper tackles an important problem of automatically fixing erroneous code snippets. The paper propose a novel application of code diffusion models to the task of code repair. They propose to directly use diffusion model reverse process to fix the erroneous code snippets and to generate training data for other code repair models, which is to my understanding a novel approach, and using diffusion models for the code repair task seems like a reasonable idea. 

Authors experiments on three languages: Python, PowerShell, Excel.

Analysis from this paper is interesting and I believe will be valuable for code community.

### Weaknesses
 - While the paper focuses on the code repairing, it is hard to understand the assumptions of this work, which types of code errors (syntax errors, compilation errors, variable misuse, interface errors, etc. ) the diffusion model is expected to fix?
- No direct comparison to any other code repair literature makes it hard to evaluate the usability of this approach and the quality of code repair.
- No details described for the finetuning of the models on the generated training data (4.3) hinders reproducibility.
- The assumptions on human cognition patterns (how humans treat code errors) are not supported by any evidence or link to the literature, which also makes the title misleading.
- The paper contains many typos and the writing is not always precise (see questions)

- as far as I understand, to repair code snippet, this work first adds a noise to it and then apply several reverse diffusion steps to reconstruct it? Why do you add additional noise to the erroneous snippet? My intuition would be that a code sample with errors is already "noisy".
- is $\epsilon$ noise in line 178, 185 the single scalar or it should be a vector/matrix? From the writing it seems that it is a scalar, but I think it should be a matrix.
- how any% best% pooled% are exactly computed? Does it mean that we sample different $\epsilon$ or different noise powers?
- How do you ensure that data from pre-training does not intersect with data used during evaluation? Do you perform any deduplication?
- Can you point to the references regarding the comparison to humans: "human error patterns", "closely mirrors how humans tackle complex problems" discussed in this work?

Typos and unclear writing:
- 029: from the distribution -> from a distribution?
- 042: not sure why "thus" is here
- 074: define "continuous human noise operator"
- define "last-mile" error
- 081: remove brackets around 56.4-68.2%
- 090 Diffusion models: typo in paragraph name; 
- clarify the family of diffusion models used in this work?
- 048: what is the notation used here, and what are the "specifications", what is $d$? $T$ here is not the same as diffusion time step I assume?
- 170: Is the loss the same as in GENIE (Lin et al.,2023)? in 1. loss part should $\epsilon_t, \hat{\epsilon}_t$ be part of the loss definition?. In 2. what is $D_s$ in loss definition?
- Figure 3: what are the bars here and how to interpret the intersection between them? I am not sure I understood this figure.
- 207: "different styles of code", I am not sure the styles is the right word here, maybe you mean programming languages?
- 251: the classification head here is a linear transformation?
- 255: which code repair task? Citation? 
- Table 1: what is Clamp vs Decoder? Maybe add citations here to Unet and Transformer (or point to where you formulate these models in detail?)
- Figure 4: I am not sure I understand the conclusion, what is Noise (%) here for X axis on the plots?
- 314: add citations for syntactic generators and gpt-4o.

### Questions
- as far as I understand, to repair code snippet, this work first adds a noise to it and then apply several reverse diffusion steps to reconstruct it? Why do you add additional noise to the erroneous snippet? My intuition would be that a code sample with errors is already "noisy".
- is $\epsilon$ noise in line 178, 185 the single scalar or it should be a vector/matrix? From the writing it seems that it is a scalar, but I think it should be a matrix.
- how any% best% pooled% are exactly computed? Does it mean that we sample different $\epsilon$ or different noise powers?
- How do you ensure that data from pre-training does not intersect with data used during evaluation? Do you perform any deduplication?
- Can you point to the references regarding the comparison to humans: "human error patterns", "closely mirrors how humans tackle complex problems" discussed in this work?

Typos and unclear writing:
- 029: from the distribution -> from a distribution?
- 042: not sure why "thus" is here
- 074: define "continuous human noise operator"
- define "last-mile" error
- 081: remove brackets around 56.4-68.2%
- 090 Diffusion models: typo in paragraph name; 
- clarify the family of diffusion models used in this work?
- 048: what is the notation used here, and what are the "specifications", what is $d$? $T$ here is not the same as diffusion time step I assume?
- 170: Is the loss the same as in GENIE (Lin et al.,2023)? in 1. loss part should $\epsilon_t, \hat{\epsilon}_t$ be part of the loss definition?. In 2. what is $D_s$ in loss definition?
- Figure 3: what are the bars here and how to interpret the intersection between them? I am not sure I understood this figure.
- 207: "different styles of code", I am not sure the styles is the right word here, maybe you mean programming languages?
- 251: the classification head here is a linear transformation?
- 255: which code repair task? Citation? 
- Table 1: what is Clamp vs Decoder? Maybe add citations here to Unet and Transformer (or point to where you formulate these models in detail?)
- Figure 4: I am not sure I understand the conclusion, what is Noise (%) here for X axis on the plots?
- 314: add citations for syntactic generators and gpt-4o.


Links: Genie, Lin et al. 2023: https://arxiv.org/pdf/2212.11685

### Soundness
3

### Presentation
2

### Contribution
3
