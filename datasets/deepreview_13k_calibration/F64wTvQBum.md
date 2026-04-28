# Shh, don't say that! Domain Certification in LLMs

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Large language models (LLMs) are often deployed to do constrained tasks, with narrow domains. For example, customer support bots can be built on top of LLMs, relying on their broad language understanding and capabilities to enhance performance. However, these LLMs are adversarially susceptible, potentially generating outputs outside the intended domain. To formalize, assess and mitigate this risk, we introduce \emph{domain certification}; a guarantee that accurately characterizes the out-of-domain behavior of language models. We then propose a simple yet effective approach dubbed VALID that provides adversarial bounds as a certificate. Finally, we evaluate our method across a diverse set of datasets, demonstrating that it yields meaningful certificates.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a theoretical foundation for certifying language models trained to produce outputs in a domain. Then the work proses VALID, an algrithm that provides provable upper bounds on out of domain behavior of language models. The method preserves a good chunk of the unconstrained LM's performance on MMLU@Med while being robust to poducing out-of-domain outputs. There are also various other experiment results on datasets like TinyShakespeare and 20NG that show the effectiveness of the method to potentially detect and certify OOD behavior of language models.

### Strengths
- Strong theoretical foundations for classifying out-of-domain behavior of language models and ways to prevent this.
- The algorithm VALID is relatively straightforward and uses rejection sampling as an elegant way to achieve the certifications.
- The empirical evidence presented is across various kinds of datasets(Tiny Shakespeare, MedQA) which shows the generizability of VALID.
- The work is novel and needed to provide theoretical insights and guarantees for safe deployment of language models.
- Well written and the progression from atomic to domain certificates is explained well.

### Weaknesses
The paper acknowledges most of the limitations, but there is still room for further discussion:
1. Lack of context for guide model G. The work does argue that potentially involving the context in the final answer could fix this issue, but then the method cannot work in cases where a user wants language model to be concise and this also increases the inference cost of models as many more tokens get sampled for the output.
2. Adversarial attacks on G/M. The work acknowledges and shows adversarial attacks this method is prone to but argues that as adversaries would need white-box access to G(line 448, 453) and so the attacks may not be feasible. White-box access does not need to hold for the success of adversarial attacks, as some attacks do generalize across various models even if they were originally targeted at some other specific model. This should be further investigated.
3. Rejection sampling with T>1  incurs an inefficiency, which could be reduced as multiple samples could be drawn in parallel. In any case, there is additional computational overhead.

### Questions
1. Is there a reason that certified benchmarking was only done on MMLU@Med? I think it would be useful to have results for other benchmarks as well.
2. Could we use a guide model G to detect whether an input is in-domain? It might be interesting to see how the likelihood of L(y|x) would change for "in-domain" and ood inputs.
3. While the authors mention certification in computer vision (line 80-81), there has been some work on certification in NLP as well, such as https://arxiv.org/abs/2401.01262, https://arxiv.org/abs/2402.15929, https://arxiv.org/abs/2403.10144v1.  I think mentions of some of these works would prevent the false impression that certification has only been applied to computer vision and provide a more complete picture of the certification work being done across domains.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work studies domain certification, which refers to the characterization of the out-of-domain behavior of language models. This paper first formaize the definition of domain certification. And then propose an approach, VALID, to achieve domain certification. The proposed approach is empirically evaluated on multiple datasets in various domains including TinyShakespeare, 20NG, MedicalQA. The experimetal results show that the proposed method is effective at achieving domain certification as defined in this work.

### Strengths
1. This work introduces and formalize domain certification for characterizing the out-of-domain behavior of language models under adversarial attach, which is useful for language models tuned a specific domain.
2. An approach called VALID is proposed to achieve domain certification. VALID bounds the probability of a LLM answering out-of-domain questions.

### Weaknesses
The main concern for this work is its limitations including the reliance on the domain generator which doesn't consider the model input. In addition, Theorem 1 assumes the certificate is useful given G is trained on in-domain data. However, as language models are usually pre-trained on large amound of text data, which ingests world knowledge into it. Therefore, model G can contains out-of-domain knowedge, which makes Theorem 1 extremely limited.

### Questions
See weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work studies the problem of adversarial certificates for LLMs in domain specific deployment contexts. They define the problem of "domain certification" and derive a test time algorithm VALID based on a small guide/reference model, and a rejection sampling criterion, that provides such domain certificates. They quantify levels of tightness and permissiveness of their certificates using real data on out of domain and in domain samples respectively to argue for the potential utility their method in real deployments.

### Strengths
1. Motivate the difficulty and real world implications of certifiable test time behavior for model LLM systems.
2. Present a simple and clear algorithm to achieve their definition of domain certification.
3. Identify a clever way to harness the limited abilities of very small, cheap to train, domain specific language models to implement test time rejection sampling favoring a constrained distribution of responses.

### Weaknesses
1. Work under very limiting constraints of a fixed set of bad strings F. This is a practical assumption, but pervasive limitation for this work and of any other attempts to characterize the output spaces of generative models with large vocabularies, and variable size outputs. See lines 132-137 for the authors' own description of this required narrowing of scope. This always leaves room for adversaries to circumvent certificates via finding inputs in the complement of the finite sample of F chosen, but still in T' such that they are falsely permitted by the system.

2. It's not immediately clear how good the D_T to D_F ratios are in Table 1. Additionally, there seems to be a correlation between success/separation and the domain similarity, which is expected? Maybe the authors can discuss this further potentially highlighting a limitation of the approach based on how well separated good and bad behaviors are in a given domain.

3. The generative results are weaker than the fixed sample set results, summarized lets say as weaker Youden's J for the same domain setting, and since this is the more realistic evaluation, it is important to caution that this approach isn't quite deployable at the moment. (On that note, lines 145-152 are more appropriate moved to the final paragraphs as a discussion section/future work/applications blurb)

### Questions
Primary question (multi-part, single theme): 

Initially, I was going to comment that training guide LLM, G, on only "good strings" in T, will not necessarily give you a model that only assigns high likelihood to strings in T, and therefore there will likely exist some strings for which both L and G assign high likelihood but are in fact in T'... however, after reaching the Section 3.1 experimental setup detail that guide models G were to be parametrized by relatively tiny gpt2 style models, it became clear how this might work in practice. 

1. As a preliminary ask, "Such a certificate with respect to G can be useful: As G is only trained on samples in DT ⊂ T, a dataset of domain T, it assigns exponentially small likelihood to samples that are in F."
Is there an analytic or empirical argument that the authors can provide for this statement? It seems like both the benign and adversarial robustness of the certificate hinge on this assumption.

Now, the section of future work describes a desire to explore using stronger models for G, which suggests that the authors don't necessarily see the _weakness of G_, eg. its inability to predict next tokens in any context beyond the small corpus on which it was fit, and maybe poorly even within that domain, as the actual crux of the method that _makes it work_. 

2. Was any ablation done about the model size for G and or the corpus size for training it? My hypothesis is that the stronger G becomes (more parameters and/or data), the wider set of strings it is able to model and therefor the closer L(y|x) and G(y) become, eventually depleting all the power of the algorithm. 

3. Overall, can the authors elaborate on any "behind the scenes" details that aren't in the draft or appendix on how G's role in the certificate was developed during the research and why the particular experimental choices (tiny gpt2's) for it were made?

Whatever the answers are to this series of questions are, in my opinion, necessary additions to the draft to improve its clarity and soundness, as well as the ability for future work to build upon these results. Currently, my takeaway centers the identification of a weak G to compute an odds ratio against L as a way to perform rejection sampling for safety and alignment, and thus pitching the results a little more in this direction potentially improves the relevance and generalizability of the work (since the particular certificates/and algorithm might be limited in immediate applicability). 

Some relevant works that abstractly leverage the same odds ratio paradigm, though for different purposes, are Contrastive Decoding by Li et al. (2210.15097) which moderates policy L via a weaker policy L' at decoding time to improve output quality, and Direct Preference Optimization by Rafailov et al. (2305.18290) as a way to train a policy L to prefer samples in T rather than T'.

Minor:

4. L257, does "OOD" mean "F"? To match L 269 referring to other question domains as "F". Generally, maybe prefer one notation or the other to refer to the "bad" set everywhere.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a method to assess and mitigate the risk of Large Language Models (LLMs) deployed in particular tasks answering out-of-domain questions, a concept/framework which they formalize as domain certification. The proposed method, VALID, provides adversarial bounds as a certificate. Finally, this method is evaluated over 3 datasets.

### Strengths
The paper is interesting, well motivated and tackles a relevant problem. 

The problem and concepts are well-defined. Domain certification is a interesting concept, and VALID's design appears well justified.   

Despite the lack of discussion and comparison on existing guardrails this method benefits from providing some type of mathematical guarantees, which is a desirable property given recent legislation (particularly in the EU), as the authors mention.

### Weaknesses
The literature review should be improved. There is little to no discussion on related methods/tasks, and existing approaches to tackle this issue (if any). For example, a greater discussion on methods regarding LLM guardrails, and how they compare to your approach. Specifically, the paper lacks a discussion on methods that attempt to restrict LLM outputs to a specific domain, or methods that detect out-of-domain outputs, and how this work differs or improves upon them. 

Domain certification always requires the definition of F, which if I understood correctly, is used for the definition of domain certification and the experimental procedure, since VALID was motivated mainly by the "certification through divergence" approach. Adding some general recommendations on the definition of F in general terms, or for applied scenarios, would be interesting (e.g., I could find vast amounts of OOD data in benchmark datasets for a tax advisory LLM, but is there an efficient way to select a representative F?)  It's unclear how to ensure that the chosen F is representative of all possible out-of-domain scenarios, and what the impact of a poorly chosen F would be on the validity of the certification.

It would be interesting to see how different definitions of the model G affect the quality of this method. For example, how does the size of the model G, or the training data used to train G, impact the tightness of the certificate? The paper should explore this sensitivity more thoroughly. 

The experimental results lack a comparison to any benchmark or baseline method. Literature on LLM guardrails could be used as a way to compare the effectiveness of this approach. In my opinion, the main and most important weakness of this paper is the experimental setup, followed by the literature review, both of which should be substantially improved. The paper needs to demonstrate the effectiveness of the proposed method compared to existing techniques, even if those techniques do not provide formal guarantees. Without this, it is difficult to assess the practical value of the proposed approach.

### Questions
- How does this method compare to setting up restrictive (already existing) guardrail methods specific to a domain/task?
- If the LLM is being deployed for a specific task (such as the tax report example used in throughout the paper), how easy is it to set up VALID? Do you use a finetuned version of L to form G? Do you use a smaller finetuned LLM? Is it trained from scratch? Is it a simple discriminator? This is something that may be clarified once source code is available, but in any case it would have been great if at least an anonymized repository was provided.  
- What is contained in F′ ∩ T′? Seems unclear to me. Only semantically incoherent sequences? 
- VALID requires a secondary language model G, trained on in-domain data. In that case, since domain data is necessary anyway, wouldn't it be simpler to just quantify similarities between an output and the in-domain corpus within an embedding space, sparing the need for secondary model trained with in-domain data?
- Around line 150, you mention "The deployer might perform an a priori risk assessment and determine that they can tolerate the consequences of one out-of-domain response from a set D_F per year." But given your method depends on F for domain certification, and VALID depends on G, are there any guarantees that only one out-of-domain response will be produced per year? Seems like a very bold claim.

### Soundness
4

### Presentation
4

### Contribution
3
