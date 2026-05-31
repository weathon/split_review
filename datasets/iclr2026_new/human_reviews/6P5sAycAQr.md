## Human Reviewer 1

### Summary
This paper organically integrates two lines of zero-shot CLIP enhancement methods—text prompt augmentation and hierarchy-based approaches—into a unified workflow to improve CLIP’s zero-shot classification performance.

### Strengths
The proposed method demonstrates a clear and rigorous workflow, supported by significant and well-validated experimental results.

### Weaknesses
The performance of the proposed method may potentially depend on the class structure of the classification task. 

Although the paper emphasizes that taxonomic context is essential for classification, there is limited analysis supporting this claim beyond the reported accuracy of the proposed method. In Table 4, removing the taxonomic context (W-TaxS) outperforms removing the descriptors (TaxCLIP) in several cases, which does not appear to substantiate the assertion that taxonomic context is essential.

### Questions
Could you please include additional experimental results comparing the proposed method with existing baselines on fine-grained benchmarks, such as Oxford Flowers 102 and Stanford Cars?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper presents a simple approach for prompt adaptation to improve zero-shot classification of Vision Language models such as CLIP. The authors propose constructing prompts with supercategories appended to prompts for each class. Evaluation is conducted over multiple benchmarks. Ablations and improvements over baselines is shown.

### Strengths
The authors show improvement over baselines for most datasets. Extensive evaluation includes performance of the method over various CLIP architecures as well as ablations over different aspects such as prompt construction choices.

### Weaknesses
Novelty is very limited. There is very little difference conceptually wrt CHiLS and CGPT-P (cited in the paper). Why have the authors decided to only include one level in their hierarchical tree? This has not been discussed. What happens if you construct a deeper tree? This also brings into concern the fact that simply appending the super category name to the class prompt should be suboptimal as CLIP often suffers with long context without specialized fine-tuning. The performance reported does not match numbers in other papers like CHiLS for some datasets. What could cause this? Table 1 does not state the numbers are for which CLIP architecture. The lack of examples of what the texts look like also leads to confusion about the reason why this approach will work better than CHiLS and CGPT-P.

### Questions
Please refer to questions in weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper introduces DefNTaxS, which addresses taxonomic ambiguity in zero-shot classification by automatically generating LLM-based taxonomic context for class prompts. Building on D-CLIP's approach of adding descriptors to class names, DefNTaxS extends the template to include subcategory information: while D-CLIP uses "[class] which [has/is] [descriptor]", DefNTaxS adds taxonomic context as "[class] which [has/is] [descriptor], [contextual phrase] [subcategory]". The method uses GPT-X to discover subcategories, assign classes (targeting ~20 classes per group), and generate natural contextual phrases, achieving +5.5% average improvement over CLIP and +2.44% over D-CLIP across seven benchmarks without requiring model retraining.

### Strengths
The work explores an interesting aspect of vision-text alignment by investigating how taxonomic context can help resolve semantic ambiguities in CLIP-style models, addressing a real limitation where classes like "boxer" could refer to dogs or athletes depending on dataset context.

### Weaknesses
-- marginal extension over existing work: The contribution is an incremental improvement over D-CLIP and related LLM-prompting methods (WaffleCLIP, CuPL, CHiLS), essentially adding one more field to existing prompt templates. The taxonomic discovery process reduces to basic LLM prompting with heuristic post-processing rules, offering limited technical novelty beyond existing descriptor-based approaches.

-- small performance gains: The improvements over D-CLIP are modest (+2.44% average, table 1) and inconsistent across datasets, with some showing minimal gains (+0.16% on Places365) or even degradation (-1.05% on Food101). 

-- limited technical and scientific contribution: the paper lacks architectural insights about vision-language models and proposes no learnable components or model modifications. The study is mainly about prompt manipulation, which doesn't advance our understanding of why CLIP struggles with ambiguity or how to fundamentally improve VLM architectures.

### Questions
--

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper extends existing works on image-text matching within VLMs such as CLIP by augmenting class descriptors with taxonomical context, achieving a gain of on average 5.5% over CLIP on standard benchmarks.

### Strengths
The paper is well written and simple to follow, and on standard benchmarks compared to methods such as D-CLIP or WaffleCLIP, consistent performance improvements can be found.

### Weaknesses
I have several issues with the proposed setup, and would love for the authors to provide more context here:
* Why would DEFNTAXS actually be a meaningful improvement over D-CLIP, which itself has significant issues, as descriptors proposed by LLMs are not necessary to be found in given query images, see Roth et al. 2023? The problems are the same, it's just that more context is provided that may or may not match the query image, no? I.e., adding "commonly found in kitchen utils" would maybe help to differentate a fork against, say, a motorcycle, but the fail when contrasting between potentially a single fork, and a general image on kitchen utensils, since redundancy is introduced.
* Importantly, a lot of additional semantic information is introduced into a language encoder that is known to be very weak and often fails to distinguish finegrained or multiples of semantic features. It would be important for the authors to offer some support that the CLIP model actually meaningfully and explicitly leverages the semantic context; and its not just better chosen structured noise which is given the additional performance gains.

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4