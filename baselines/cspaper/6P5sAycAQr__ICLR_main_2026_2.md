---
job_id: f6d665b4-0087-49b7-9804-c50a04b906be
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 6P5sAycAQr.pdf
paper: DEFNTAXS: The Inevitable Need for Context in Classification
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is directly about zero-shot image classification with CLIP-style vision-language models, prompt construction, and semantic/taxonomic context, which fits representation learning and vision-language learning at ICLR.

## Minimum Quality
Pass ✅ The paper contains the required scientific structure, including Abstract, Introduction, Related Work, Method, Experiments, Results, Ablations, and Conclusion. While I have substantial concerns about novelty, overclaiming, and experimental methodology, these rise to the level of reviewable weaknesses rather than an obvious desk-reject threshold.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find hidden instructions, suspicious reviewer-targeted text, or other manipulative content in the provided manuscript.

# Expected Review Outcome:
## Summary
This paper proposes DefNTaxS, a training-free procedure for zero-shot image classification with CLIP that augments class prompts using LLM-generated taxonomic subcategories in addition to class-specific descriptors. The method first groups dataset classes into subcategories, assigns each class to one such group, optionally refines group granularity, and then produces prompts of the form class + descriptor + contextual taxonomic phrase. Experiments on seven benchmarks show improvements over vanilla CLIP and several prompt-based or hierarchy-based baselines, with especially large gains reported on EuroSAT.

## Strengths
The paper addresses a real and practically relevant issue in zero-shot classification, namely label ambiguity and insufficient contextualization of class names. The motivating examples in the introduction, such as “boxer,” “crane,” and “mouse,” are intuitive and make the problem setup easy to grasp.

The proposed pipeline is simple, fully automated, and easy to deploy. In settings where users already rely on CLIP-style zero-shot classification, a training-free prompt-construction method with low monetary cost is attractive. The claimed total text-generation cost of $0.38 on Page 5 is practically appealing.

The empirical scope in the main paper is reasonably broad. Table 1 evaluates seven datasets plus ImageNetV2, and the method outperforms vanilla CLIP on all reported datasets, with notable gains on Pets and EuroSAT. Even if some gains over stronger baselines are modest, the overall pattern does suggest that adding contextual taxonomic information can help.

Some ablations are useful and go beyond a single headline table. In particular, Table 3 is informative because it probes the role of the two main prompt components. The “no desc.” row shows that a substantial fraction of the gain survives even when class-specific descriptors are removed, which supports the paper’s claim that taxonomic context, not only fine-grained descriptors, contributes meaningfully. Conversely, the “tax. desc.” row shows that more text is not automatically better, which is a helpful negative result.

The paper includes several conceptual and empirical figures that are relevant to the claims. Figure 4 is a useful conceptual visualization of how adding descriptors alone can still leave semantically overlapping prompts close in embedding space, whereas adding a taxonomic relation may separate them. Figure 2 is also valuable because it reveals that the choice of subcategory size matters, rather than this being an arbitrary implementation detail.

## Weaknesses
1. **The paper substantially overstates what has been established, especially the repeated claim that taxonomic context is “essential” or a “fundamental requirement.”**  
   This is the most important issue for me. The title, abstract, introduction, results, and conclusion all push a very strong causal thesis, for example “the inevitable need for context in classification,” “taxonomic context is not merely helpful but essential,” and “fundamental requirement for robust zero-shot image classification” (Pages 1, 2, 6, 9). The evidence in the paper does not support a claim at that strength. What the experiments show is that one particular prompt-engineering scheme often improves top-1 accuracy over several baselines on a set of benchmarks. That is materially weaker than showing necessity or inevitability.  
   This matters because the manuscript is written as if it is settling a broad conceptual question, while the actual evidence is a set of empirical comparisons for a specific automated prompting pipeline using CLIP and GPT-generated text. A more defensible framing would be that taxonomic context is a useful and often underexplored source of prompt information, not that it has been shown to be essential in general.

2. **Novelty is limited relative to existing LLM-based prompt augmentation and hierarchy-aware CLIP methods.**  
   The core method is a procedural combination of familiar ingredients: generate descriptors with an LLM, generate higher-level semantic groupings with an LLM, append those groupings to prompts, and average similarities across prompts. This is close in spirit to combining descriptor-based methods like D-CLIP with taxonomy/hierarchy-aware methods like CHiLS and CGPT-P. The paper does state this combination, but it does not sufficiently convince me that the methodological step itself is more than an incremental extension.  
   The issue is not that incremental work is invalid, but that the paper is positioned as a conceptual advance rather than a prompt-format variant with heuristic LLM post-processing. The contribution could still be acceptable with very strong analysis or especially compelling evidence, but in its current form it overclaims relative to the level of technical novelty.

3. **The method description is not precise enough to be scientifically satisfying, especially around the LLM-driven assignment/refinement loop.**  
   Section 3 presents a four-step pipeline, but crucial parts remain underspecified:
   - In Section 3.2, if a class can belong to multiple subcategories, the paper says it is assigned to the “most unique/least likely subcategory,” but this criterion is not operationally defined in the main text.
   - The “edge case” handling on Page 4 is especially concerning. The paper says that if the dataset contains both dog and sport senses of “boxer,” the method checks for an already assigned subcategory and instructs the LLM to avoid that subcategory, “looping until a unique assignment is found.” This sounds like an ad hoc conflict-resolution rule, but there is no algorithmic specification, termination argument, or discussion of failure cases.
   - In Section 3.3, the refinement procedure is guided by a target of about 20 classes per subcategory, but the actual splitting and stopping criteria are not defined rigorously in the main text. The paper relies on Appendix D for this choice, but the core procedure still needs to be clearer in the main body if it is central to the method.
   
   This matters because the proposed contribution is not a learned model but a procedure. If the procedure is heuristic and LLM-sensitive, then the exact prompting, retry logic, and refinement rules become the method. Right now, the paper gives the flavor of the pipeline but not a sufficiently crisp algorithmic specification.

4. **The mathematical presentation is very thin, and the equations do not really formalize the method’s key decisions.**  
   Equation (1) on Page 3 merely states that the subcategories form a partition of the class set. That is fine as a set-theoretic condition, but it does not specify how the partition is obtained or what objective it optimizes. The paper claims the method discovers subcategories that “maximize inter-class differentiation” and are “task-relevant,” yet there is no optimization problem, scoring function, or criterion written down that corresponds to this claim.  
   Equations (2) and (3) on Page 5 are also standard averaging-and-argmax inference formulas. They define
   \[
   \text{Score}(c)=\frac{1}{|D_c|}\sum_{d\in D_c}\text{similarity}(\text{image}(x),\text{text}(\text{prompt}(c,d))),
   \]
   but several implementation choices that can affect results are omitted: what exact similarity is used, whether embeddings are normalized, whether CLIP logit scaling is retained, and whether prompt ensembling uses logits or cosine similarities before averaging. Since the paper’s contribution is entirely in test-time prompt construction, these details are not cosmetic.
   
   More importantly, the equations completely omit the taxonomic assignment and refinement mechanism, which is the actual novelty claim. The formalism therefore gives a misleading sense of rigor around peripheral parts while leaving the central decision process informal.

5. **Experimental methodology raises concerns about possible benchmark-specific tuning and lack of a clean model-selection protocol.**  
   On Page 5, Section 4.1 states that “classification accuracy is reported as the primary evaluation metric in a pure zero-shot setting on each dataset’s standard training split.” This sentence is confusing at best, because evaluation is usually on a test split or standard zero-shot evaluation split, not “the standard training split.” If the paper indeed evaluates on training data, that would be a serious issue; if not, the wording needs correction immediately.  
   Separately, the choice of “approximately 20 classes per subcategory yields optimal results” in Section 3.3 is based on empirical analysis, but the paper then applies this choice across datasets in the main evaluation. Since the same benchmarks are used to motivate and validate this hyperparameter-like heuristic, the paper should clarify whether this was selected globally before final experiments, whether it was tuned per dataset, and whether any held-out validation protocol was used. Figure 2 suggests meaningful sensitivity to this parameter, so this is not a negligible detail.  
   This matters because in a fully training-free setting, prompt construction and prompt-length heuristics effectively become the tuning knobs. Without a clearer protocol, it is hard to distinguish a generally valid method from benchmark-specific prompt engineering.

6. **The main comparative gains over the strongest baselines are more modest and less uniform than the narrative suggests.**  
   Table 1 looks good at first glance, but the paper’s framing leans too heavily on the average gain over vanilla CLIP rather than the more meaningful comparison to stronger prompt-based baselines. Against D-CLIP, the average gain is +2.44, and the improvements on some datasets are quite small, for example +0.48 on ImageNet, +0.16 on Places, and +0.66 on ImageNetV2. On Food, DefNTaxS is behind CHiLS (81.48 vs 83.53). On Places, it is behind CHiLS and barely above D-CLIP and CGPT-P.  
   This does not invalidate the paper, but it tempers the strength of the empirical claim. The paper repeatedly talks as if it has clearly established a dominant new principle. Table 1 instead supports a more modest interpretation: the method is often helpful, sometimes clearly helpful, but not uniformly transformative relative to the strongest baselines.

7. **The ablations partly undermine the paper’s semantic interpretation, and the analysis does not wrestle with that deeply enough.**  
   Table 4 is particularly important here. W-TaxS, which substitutes taxonomic labels with random characters while retaining the class descriptor, is slightly better than DefNTaxS on ImageNet, CUB, and Places, and only somewhat worse on several others. TaxCLIP, which substitutes class descriptors with random characters while retaining taxonomic labels, is also competitive on several datasets. The paper acknowledges “mixed results,” but the implications are more serious than the discussion suggests.  
   If random tokens can preserve much of the gain, then the current evidence does not cleanly separate “semantic taxonomic understanding” from generic prompt differentiation or token-position effects. The paper mentions this possibility, but then still concludes with very strong semantic claims. That is too convenient.  
   Relatedly, Table 12 shows that even randomly grouped subcategories can remain fairly competitive, sometimes within error bars of the proposed method. This is a serious warning sign that some of the benefit may come from adding structured differentiation noise rather than accurate taxonomy per se. The paper notes the increased variance, but the conclusion should be much more cautious.

8. **Figure-based evidence is used selectively, and some figures actually point to limitations that the paper does not integrate into the main conclusion.**  
   Figure 2, which studies subcategory size, does not show a universally clean “20 classes is optimal” story. The trends differ by dataset, and some curves are noisy or relatively flat. Yet Section 3.3 elevates the approximate 20-class rule into a general design principle. The figure supports “dataset-dependent sensitivity with a rough plateau in some cases,” not a strong universal prescription.  
   Figure 3 is also more ambiguous than the surrounding text implies. On several datasets, accuracy degrades as randomization increases, which is good evidence that assignments matter. But on DTD and Food the changes are much less decisive, and the variance seems substantial. Again, this is compatible with the method being useful, but it does not support the stronger narrative that accurate taxonomic semantics are the dominant explanatory factor in all settings.  
   In contrast, Figure 1 is helpful as a pipeline illustration, but it also highlights the simplicity of the method: LLM-generated categories, descriptor generation, assignment, then a prompt template. That simplicity is not a flaw by itself, but it reinforces the need for stronger evidence and sharper analysis if the paper wants to claim a major conceptual advance.

9. **Some baseline handling and reporting choices are not convincing enough.**  
   On Page 6, the paper says all baselines were recreated using the setup in Section 4.1 and “all potential variables were maintained strictly to those used in the original studies.” That is a strong claim, but the paper also says descriptors were generated using a modified version of D-CLIP’s pipeline because GPT-3 API was deprecated. These two statements are in tension. If prompts or LLM outputs differ materially from those in the original papers, then baseline replication fidelity is limited, and this should be discussed more openly.  
   Also, most main results in Table 1 are presented as single numbers without variance, even though later tables such as Table 4 and Table 12 report means and standard errors across runs. Since LLM-based text generation can be nondeterministic and the random-token baselines clearly have variance, more consistent uncertainty reporting would improve trust in the comparisons.

10. **Presentation quality is uneven, with several wording, notation, and consistency issues.**  
   There are numerous places where the exposition feels closer to a persuasive project report than a polished scientific paper. Examples include overconfident rhetorical phrases, inconsistent naming, and small but distracting issues in tables and text. A few examples:
   - Section numbering around “3.5 Building the Final Text Prompts and Classification” is missing the usual subsection formatting.
   - Table numbering and surrounding references are a bit confusing in Section 6.1, where the text introduces one table and then shifts to another.
   - Appendix tables contain multiple naming inconsistencies or likely typos, for example “CUR,” “Priv,” “EXAT,” “W-CLIPcorrecept,” and “DeiNToeS” in Table 10. Even though these are outside the main body, they reduce confidence in the care taken throughout.
   - Several claims are stated more strongly than the underlying data support.
   
   None of these issues alone is fatal, but together they weaken confidence and clarity.

11. **The literature positioning is incomplete for a paper making broad claims about taxonomy-aware prompting and hierarchical semantics.**  
   The paper cites D-CLIP, WaffleCLIP, CuPL, CHiLS, and a ChatGPT-powered hierarchical comparison method, which are relevant. However, for a paper centered on taxonomy-aware prompting and hierarchy-informed zero-shot classification, the positioning still feels narrow. The manuscript should do a better job distinguishing its contribution from prior hierarchy-aware prompting approaches and taxonomy-based zero-shot methods more broadly, especially since the central idea is precisely to encode higher-level class structure into text prompts.  
   I am not penalizing the paper for not citing everything under the sun, but given how aggressively it claims to identify a missing principle in the literature, the related-work section should be more comprehensive and more precise about what is truly new here.

## Questions
1. The sentence in Section 4.1 saying evaluation is performed “on each dataset’s standard training split” is potentially very serious. Please clarify exactly which split is used for each dataset, and whether any test data were used in selecting prompt-construction heuristics such as the 20-classes-per-subcategory rule.

2. Can the authors provide a precise algorithm, preferably pseudocode in the main paper, for the assignment/refinement loop in Sections 3.2 and 3.3? In particular:
   - how ties or multi-sense classes are resolved,
   - how many retries are allowed,
   - what happens if the LLM keeps proposing previously used or overly broad subcategories,
   - and whether the process is deterministic.

3. Please quantify sensitivity to the choice of LLM. Since the entire method depends on GPT-4o-mini for taxonomy generation, how robust are the final results if one uses another modern LLM or different decoding seeds? This would materially affect my confidence that the method is not overly tied to one API behavior.

4. Can you separate the effects of semantic correctness versus mere prompt differentiation more cleanly? Table 4 and Table 12 suggest that random or weakly meaningful strings/groupings retain a nontrivial portion of the gain. A stronger analysis, for example correlation between assignment quality and accuracy across datasets or manually verified subsets, would help.

5. Table 1 should ideally be supplemented with uncertainty estimates, at least for DefNTaxS and the strongest baselines. Are the reported gains over D-CLIP and CGPT-P statistically stable across multiple prompt generations?

6. Figure 2 suggests dataset-dependent sensitivity to subcategory size rather than a universally optimal value of 20. Can the authors clarify whether this threshold was chosen globally in advance or after observing benchmark behavior, and whether a fixed threshold of 20 is really the right recommendation?

7. The paper’s headline conceptual claim would be stronger if accompanied by error analysis. For example, among images corrected by DefNTaxS relative to D-CLIP, how many involve genuinely ambiguous class names or semantically neighboring classes? This could help determine whether the method truly resolves ambiguity rather than just altering prompt statistics.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work is a prompt-engineering method for benchmark classification and does not introduce obvious new risks beyond standard concerns around reliance on proprietary LLM APIs for text generation.

## Soundness Rating
2: fair. The empirical results suggest the method can help, but the central conceptual claims are stronger than what the evidence supports, and key parts of the LLM-driven procedure are insufficiently specified.

## Presentation Rating
2: fair. The paper is readable and motivated, but it overstates conclusions, leaves important procedural details underspecified, and has several consistency and exposition issues.

## Contribution Rating
2: fair. The method is a useful practical combination of existing prompt-engineering ideas, but the technical novelty and scientific insight are limited relative to the paper’s framing.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and practically useful, and the empirical gains are real enough to take seriously, but the current submission overclaims, underspecifies the core procedure, and does not cleanly establish that the reported improvements arise from taxonomic semantics rather than more generic prompt differentiation effects.

## Reviewer Confidence
4: confident. I am confident in this assessment, though it is still possible that some implementation details not fully captured in the main paper would clarify a few concerns.