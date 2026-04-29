# Fodor and Pylyshyn’s Legacy – Still No Human-like Systematic Compositionality in Neural Networks

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
Strong meta-learning capabilities for systematic compositionality are emerging as an important skill for navigating the complex and changing tasks of today's world. However, in presenting models for robust adaptation to novel environments, it is important to refrain from making unsupported claims about the performance of meta-learning systems that ultimately do not stand up to scrutiny. 
    While Fodor and Pylyshyn famously posited that neural networks inherently lack this capacity as they are unable to model compositional representations or structure-sensitive operations, and thus are not a viable model of the human mind, Lake and Baroni recently presented meta-learning as a pathway to compositionality. 
    In this position paper, we critically revisit this claim and highlight limitations in the proposed meta-learning framework for compositionality.
    Our analysis shows that modern neural meta-learning systems can only perform such tasks, if at all, under a very narrow and restricted definition of a meta-learning setup. 
    We claim that `Fodor and Pylyshyn's legacy' persists, and to date, there is no human-like systematic compositionality learned in neural networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper revisits Fodor & Pylyshyn’s 1988 claim that neural nets lack human-like compositionality. It focuses on Lake & Baroni’s 2023 meta-learning seq-to-seq benchmark, rewrites its hidden grammars into a clear pseudo-language, and reruns the released transformer ten times per episode, exposing big accuracy drops and rule inconsistencies.

Key contributions: (i) pinpoints which parts of the Fodor–Pylyshyn critique the benchmark tackles; (ii) empirically shows the model confuses ‘twice’/‘thrice’, mis-parses nested ‘before/around’ strings, and fails beyond length-10 inputs; (iii) sets evaluation criteria—full out-of-distribution ablations or direct inspection of learned codes; (iv) proposes training that merges meta-learning with symbolic memory and iterative self-checking.

The paper’s stance is that the legacy stands: as of 2025 no neural network, meta-learner included, shows human-level compositionality. Real progress, it argues, will come from hybrid models able to store, manipulate and test symbolic rules within neural systems, not from simply scaling one-shot transformers.

### Strengths
The paper’s main virtue is that it restates the 1988 Fodor-Pylyshyn challenge and pin-points exactly which parts Lake-Baroni tackle, giving readers a sharp conceptual map before any experiments.

It then faithfully re-runs the public transformer on the same meta-learning episodes, with multiple seeds, and releases full episode-level outputs, so every empirical claim is reproducible and audit-able.

Beyond headline accuracy, the authors recode the hidden grammars into a readable pseudo-language and count unseen rule combinations, revealing that only 179 / 200 validation episodes are novel—a meticulous diagnostic that shows where generalisation really fails.

They further distil two concrete evaluation rules—do exhaustive OOD ablations or directly inspect learned codes—and propose “reflective learners” that iteratively verify and self-correct symbolic hypotheses, pointing to a constructive research agenda.

Each negative result (e.g., confusion of twice/thrice, breakdown beyond length 10, errors on nested before/around) is backed by the published logs, keeping the narrative tight and the reasoning easy to follow even for sceptical readers.

### Weaknesses
The study tests only Lake-Baroni’s single seq-to-seq benchmark; adding tasks that vary modality, grammar family, and noise would show whether the critique generalizes.

Results come from ten random seeds without confidence intervals or statistical tests, so readers cannot judge robustness or effect size.

The evaluation caps inputs at 10 tokens and outputs at 8 colors, preventing any look at true productivity or deep nesting limits .

Manual pseudo-language “decoding” risks researcher bias; an automated grammar-induction baseline could verify the claimed mis-parses.

Only the released transformer is re-run; including memory-augmented nets, symbolic decoders, or large instruction-tuned LLMs would ground the comparison.

Focus stays on linguistic rules; alternative views note that compositional meta-learning might manifest differently in vision or motor domains, which the paper sidelines .

Recent work finds emergent systematic skills in scaled LLMs; benchmarking such models could illuminate whether scale, not hybrids, closes the gap.

Clarifying falsifiable hypotheses, releasing code for the reflection loop, and varying support size, OOD length, and architecture would make the argument sharper and more actionable.

### Questions
1. You report means over ten random seeds but no confidence intervals or hypothesis tests. Could you provide formal statistics (e.g., bootstrap CIs or paired t-tests) so we can gauge the reliability of the observed accuracy drops?

2. Your pseudo-language “decoding” is manual. How was inter-annotator agreement measured, and could an automated grammar-induction baseline validate the identified mis-parses to dispel concerns about confirmation bias?

3. Inputs are clipped at 10 tokens and outputs at eight color symbols. Have you experimented with longer sequences to reveal whether errors grow gradually or appear abruptly at a specific depth/length threshold?

4. The study reruns only the original transformer. Why not include memory-augmented nets or large instruction-tuned LLMs (which might implicitly build symbolic caches) to test whether scale or architectural tweaks narrow the gap Fodor & Pylyshyn highlight?

5. Many recent works quantify compositionality with information-theoretic or topographic metrics rather than accuracy alone. Would adopting such metrics change your conclusions, and can you share raw model representations to facilitate third-party analysis?

### Presentation
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
This paper argues that neural networks still fail to achieve human-like systematic compositional generalization. To support this view, the authors assess Lake and Baroni’s claim and highlight that their MLC framework lacks key elements necessary for making substantive assertions about systematic generalization. The experimental results reinforce the authors' argument.


**Others**

I reviewed this paper during the ICML track. The authors have made substantial revisions compared to their previous submission, resulting in a clearer and more accessible presentation. Given these improvements, along with the significance of the problem and the value of the contribution, I support the acceptance of the paper this time.

### Strengths
1. This paper is well-written overall. The authors clearly outline the history of studies on compositional generalization and recent works, providing a strong background. 
2. The authors present substantial evidence demonstrating the limitations of the MLC framework.
3. Understanding systematic compositionality is crucial for identifying the limits of neural network intelligence.

### Weaknesses
This paper can be broadly divided into two parts: (1) a discussion on the limitations of neural networks in handling compositionality, and (2) a perspective on meta-learning systems.

However, two main issues arise: (1) the connection between the two parts is rather weak, and (2) while the first part presents clear evidence, the second part lacks strong, convincing arguments to support its claims.

### Questions
1) The author claims that "Besides both previous failure modes that are related to incompetence in extracting information from the support examples"(line 208), I am not sure why the author comes to this conclusion.

2) What's the definition of non-systematic error (line 255)

### Presentation
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Authors take the view that neural networks have not actually demonstrated human-like compositionality in spite of progress, and in particular, it critiques Lake and Baroni's recent meta-learning framework, suggesting that although they seem to find generalization, this actually reflects memorization of certain patterns in narrow settings. They suggest that evaluations using out‑of‑distribution stress tests and also explicit representations that can be inspected in order to help models avoid non-systematic errors.

### Strengths
- Clear reproducible critique about an important perspective from Lake and Baroni
- Broad context across both classical cognitive arguments and modern deep learning
- Very actionable criteria and suggestions for how we can build better meta-learners

### Weaknesses
- Very limited set of evidence from a single model and type of benchmark family
- The idea of a non-systematic error is not 100% clear and defined
- Limited evidence that neor-symbolic approaches or RL-guided reasoning could help

### Questions
- How would you formally define and quantify a non-systematic error versus a more broadly wrong rule hypothesis? 
- To what extent does this criteria apply to other tasks where symbols are less well crystallized and where composition is more fluid? 
- What are toy experiments or scaffolds which would demonstrate that neuro-symbolic approaches can be helpful here?

### Presentation
2
