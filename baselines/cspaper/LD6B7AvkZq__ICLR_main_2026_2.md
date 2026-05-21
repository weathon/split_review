---
job_id: d9c17932-a417-4f72-af8f-d50c70972f18
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: LD6B7AvkZq.pdf
paper: Unraveling Syntax: How Language Models Learn Context-Free Grammars
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly in scope for ICLR, at the intersection of language modeling, formal languages, learning dynamics, representation analysis, and learning theory.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, formal methodology/theory, experiments, quantitative results, and discussion. While there are important technical and presentation problems, they do not rise to the level of an immediate desk rejection based on the provided text alone.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious prompt-targeting text, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies how autoregressive language models trained on probabilistic context-free grammars relate to the grammar’s “subgrammar” structure. The authors define inner and outer subgrammars, derive recursive decompositions of KL divergence / language modeling loss over these substructures, and run controlled experiments with small transformers to examine whether subgrammars are learned sequentially or in parallel, whether subgrammar pretraining changes internal representations, and whether models generalize to deeper recursion.

## Strengths
The paper asks an interesting and worthwhile question. Using CFGs as a controlled setting for studying learning dynamics is a sensible approach, and focusing on subgrammar structure gives the work a clear angle rather than treating CFG learning as a single undifferentiated task.

The decomposition viewpoint is conceptually appealing. Even though I have concerns about the mathematical presentation and some claims, the central intuition, namely that LM loss over a PCFG can be broken down according to grammatical substructure, is useful as an organizing lens for experiments.

The empirical setup is reasonably coherent with the stated goals. The paper does not merely show final accuracies, it attempts to connect learning curves to specific grammatical components. In particular, **Figure 1** is one of the more effective parts of the paper: both panels visually support the claim that the total KL decreases together with the KLs of component subgrammars, and the curves suggest parallel progress rather than a clean stage-wise mastery of simpler parts first. Even if one disputes how strong the conclusion should be, the figure does communicate the phenomenon the paper wants to emphasize.

The paper also goes beyond pure performance and tries to probe internal representations. **Table 1** is useful in that it separates attention and MLP CKA, compares scratch vs pretraining, and contrasts full-grammar vs subgrammar-only evaluation. The attention-side increases after pretraining are at least suggestive that pretraining changes representational organization in a structured way, rather than only shifting final loss slightly.

The generalization section addresses a real weakness of current models on formal languages, namely recursion depth. **Figure 3** is a clear qualitative result: prediction error remains low when length increases without extra recursive depth, but grows substantially when depth increases. That contrast is arguably the strongest empirical message in the paper.

## Weaknesses
1. **There are serious mathematical and notation issues in the core derivations, and they are not cosmetic.**  
   The derivation on **Page 5, Equations (1) to (4)** is problematic in multiple ways. First, the KL expansion seems algebraically wrong. From
   \[
   D_{\mathrm{KL}}(P\|Q)=\sum_x P(x)\log \frac{P(x)}{Q(x)},
   \]
   expanding autoregressive factors should yield sums of log differences, not ratios of logarithms as written in **Equation (4)**. The displayed line
   \[
   \frac{\log P_G(\alpha|\epsilon)}{\log Q_\theta(\alpha|\epsilon)} + \sum_a P_G(a)\frac{\log P_G(a)}{\log Q_\theta(a|\alpha)} + \cdots
   \]
   is not a valid consequence of the previous lines. It should be something like a sum of terms of the form
   \[
   \sum_a P(a)\big(\log P(\cdot)-\log Q(\cdot)\big),
   \]
   or equivalently conditional KL terms, not quotients of logs. This is not a minor typo because these equations motivate the main recursive decomposition in Section 4.

   Relatedly, **Definition 4.2** is underspecified and likely malformed. It defines
   \[
   D_{\mathrm{KL}}(P_G\parallel Q)_A=\sum_{s\in\Sigma^*}P(s|\epsilon)P_G(A|s)\sum_{a\in\Sigma^*}D_{\mathrm{KL}}(P_G\parallel Q(\cdot|s)),
   \]
   but the inner sum over \(a\) is strange because the KL term itself no longer depends on \(a\). If the intent is a context-averaged KL over strings generated by \(A\), then the formula needs to explicitly define the support and distribution over those strings, for example something closer to
   \[
   \sum_s P_G(s)P_G(A|s)\sum_{a\in L(A)} P_A(a)\log\frac{P_A(a)}{Q(a|s)}.
   \]
   As written, the object being decomposed is not cleanly defined.

2. **Some foundational definitions and statements are inconsistent or imprecise, which undermines confidence in the theory.**  
   On **Page 4, Definition 3.8**, Shannon entropy is defined as
   \[
   H(P)=\mathbb{E}_{s\sim P}[\log P(s)],
   \]
   missing the minus sign. Then **Proposition 3.9** in the main text states
   \[
   \mathcal{L}(\theta)=D_{\mathrm{KL}}(P\parallel Q_\theta)+H(P),
   \]
   whereas the appendix proof on **Page 13, Equations (6) to (9)** derives
   \[
   \mathcal{L}(\theta)=D_{\mathrm{KL}}(P\parallel Q_\theta)-H(P).
   \]
   Because the entropy definition itself has the wrong sign, the two forms become ambiguously related. This is exactly the sort of basic identity that should be airtight in a theory-focused paper.

   There are also repeated theorem-numbering inconsistencies. On **Page 5**, Theorem 4.3 is stated, but on **Page 6** the text repeatedly refers to “Theorem 4.2” when discussing the same decomposition. This is a presentation problem, but in a paper where theorems are the main contribution it matters.

3. **The “unique decomposition” theorem is stated too broadly relative to the proof sketch provided.**  
   **Theorem 4.1** claims: “Every PCFG can be uniquely decomposed into a hierarchy of its inner subgrammars.” The proof sketch in the appendix on **Page 13** is much more like a recursive construction than a uniqueness proof. It does not really establish uniqueness in a mathematically robust sense. For instance, uniqueness would require clarifying what counts as the same decomposition, how node labels by sets of nonterminals avoid ambiguities due to equivalent closures, and whether isomorphic DAG representations are considered identical. None of that is addressed. A claim of uniqueness is stronger than “one can recursively construct a DAG,” and the current proof does not justify the stronger wording.

4. **The empirical claims are stronger than the evidence supports, especially around “parallel learning” and “definitively” aligned representations.**  
   The paper repeatedly claims that small transformers “learn subgrammars in parallel.” The visual evidence in **Figure 1** and **Figure 2(a)** is suggestive, but it is not sufficient to establish a mechanistic learning claim. Simultaneous decrease of several KL components does not imply genuinely parallel acquisition in any strong sense. It could also reflect shared parameter updates reducing all losses together, trivial coupling through token statistics, or the fact that these decomposed quantities are not independent objectives.

   The informal **Corollary 4.7** on **Page 7** is also too weak to rescue this claim. It essentially says that if gradient updates on one subgrammar do not hurt the others, then all are learned in parallel. That is close to a tautological sufficient condition, and no experiment actually tests whether the condition holds. So the paper’s most rhetorically prominent empirical conclusion is not sharply identified.

   Similarly, in Section 5.2 the paper says the CKA analysis shows “quite definitively” that pretraining leads to internal representations reflecting grammar substructure. That is much stronger than what **Table 1** supports. The table shows moderate shifts in average CKA, especially in attention layers, but MLP results are mixed or slightly negative in some settings. This is interesting, not definitive.

5. **The experiments are narrow and baseline-poor for the breadth of claims made.**  
   Most experiments use tiny grammars and small transformers. That is fine for controlled study, but then the paper should be more careful not to overgeneralize to “how language models acquire syntax” at large. The title and abstract frame the work broadly, yet the evidence is almost entirely from a handful of synthetic PCFGs.

   There are also very few architectural or training baselines. The appendix lists one-layer, two-layer, and four-layer variants in **Table 2**, but the main paper does not systematically compare architectures, optimizers, curriculum variants, or non-transformer baselines. If the paper wants to make claims about learning dynamics rather than merely about one specific family of tiny decoder-only transformers, more breadth is needed.

   This matters because several conclusions might be architecture-dependent. For example, the “parallel learning” effect might be a byproduct of overparameterization or of the particular training regime. The paper itself hints at this on **Page 8**, but does not evaluate it.

6. **The results tables and figures are interesting, but they are not analyzed with enough statistical or experimental rigor.**  
   **Table 1** reports average CKA across 30 random seeds, which is good, but it gives no variability estimates, no statistical tests, and no layer-wise breakdown beyond the coarse attention/MLP split. Some reported changes are small, particularly on the MLP side. Without confidence intervals or standard deviations, it is hard to judge whether the observed differences are robust or whether only the attention-layer changes are substantial.

   Likewise, **Figure 6** in the appendix shows distributions of final KL for scratch vs pretraining, and the text says pretraining “consistently shifts the distribution toward lower KL.” However, the main paper does not quantify effect sizes, significance, or sensitivity to pretraining duration beyond a light discussion. Given that the central practical claim in Section 5 is that subgrammar pretraining can help small models, the evidence should be more than boxplots and qualitative statements.

7. **The generalization section mixes a clean synthetic result with a much weaker anecdotal claim about frontier LLMs.**  
   The nested-parentheses experiment is focused and useful. However, the GPT arithmetic discussion on **Page 10** is anecdotal to the point of being scientifically weak. The paper reports performance on only \(5/5\) non-deep and \(2/5\) deep examples, with no prompt details, no temperature / decoding protocol, no repeated trials, and no reason to believe arithmetic-expression evaluation isolates the same phenomenon as the PCFG experiments. This portion reads more like a teaser than evidence, and it weakens the overall paper because it gestures toward broader relevance without adequate support.

8. **Presentation quality is below the standard needed for a theory-heavy ICLR paper.**  
   The manuscript has a large number of typographical and editorial issues: “Kulback-Leibler” on **Page 2**, “expeirmentally” on **Page 2**, “sutdy” on **Page 2**, “interet” on **Page 3**, inconsistent use of \(S\) vs \(\mathcal{S}\), missing minus signs, theorem-number mismatches, and awkward or malformed equations. The references section is also visibly messy in the provided text, with broken entries and inconsistent formatting around **Pages 11 to 13**. Individually these are minor, but collectively they make the paper feel under-polished and make it harder to trust the exact formal claims.

9. **The paper’s positioning against prior work is incomplete and sometimes overstated.**  
   The related work cites several relevant papers, including Allen-Zhu and Li and Cagnetta and Wyart, which is good. But the manuscript still tends to present its direction as more unexplored than the evidence in its own related-work section suggests. There is a meaningful difference between “little has been shown” and “this exact subgrammar decomposition framing is new,” and the paper would be stronger if it were more precise about that distinction. As written, the novelty narrative occasionally overreaches.

## Questions
1. Please carefully revise the mathematics in **Section 4**, especially **Equations (1) to (5)** and **Definition 4.2**. Can you provide a corrected formal definition of the restricted KL term \(D_{\mathrm{KL}}(P_G\|Q)_A\), including the exact support, conditioning, and averaging over contexts? A rebuttal that only says “there is a typo” will not be enough here, because the current equations appear structurally incorrect.

2. For **Theorem 4.1**, what exactly is meant by “unique decomposition”? Unique up to graph isomorphism, unique up to labeling by closures of nonterminals, or something else? Please provide a formal uniqueness statement and the missing argument.

3. For the “parallel learning” claim, can you provide a more operational metric than visual co-decrease in **Figure 1**? For example, one could measure when each subgrammar KL reaches a fixed fraction of its initial value, or compare whether simpler subgrammars systematically converge earlier than supergrammars across seeds and grammars.

4. Regarding **Table 1**, please report variability across the 30 seeds, ideally with confidence intervals or standard deviations, and clarify whether the CKA increases are statistically reliable for both attention and MLP blocks. Right now, some of the language in Section 5.2 is much stronger than the table warrants.

5. For the pretraining benefit claim, can you clarify exactly which model sizes and grammars show improved final KL, and by how much? The main text says this happens for smaller models but not larger ones; a compact summary table of final loss differences across model sizes would make this much easier to assess.

6. In **Figure 3**, the depth-vs-length contrast is compelling. Can you confirm whether the compared contexts are matched in token-level frequency or at least evaluated under a controlled distribution shift? This matters because “depth” and “rarity” may be partly confounded.

7. I would recommend either removing the frontier-LLM anecdote on **Page 10** or turning it into a proper experiment with enough samples, fixed prompts, repeated runs, and a clearer connection to the formal-language setup. Is there stronger evidence you can provide here?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission. The work uses synthetic grammars and analysis of model behavior, with no human-subjects data or obvious privacy, fairness, or safety issues discussed in the main paper.

## Soundness Rating
2: fair. The paper contains interesting ideas and some suggestive experiments, but the central mathematical presentation has notable errors and ambiguities, and several claims are stronger than the evidence currently supports.

## Presentation Rating
2: fair. The paper is readable at a high level, and several figures are helpful, but the formal exposition, notation, theorem references, and editorial polish need substantial improvement.

## Contribution Rating
2: fair. The subgrammar framing is interesting and worth discussing, but the combination of shaky formal presentation, limited experimental depth, and overclaimed conclusions keeps the overall contribution below the level I would expect for a clear ICLR accept.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a genuinely interesting angle and some promising empirical observations, especially the depth-vs-length generalization contrast and the subgrammar-focused lens. However, the current version has too many issues in the core theory, too much overstatement relative to the evidence, and not enough experimental rigor to support a positive recommendation.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main technical claims and equations in the paper, and the concerns above are based on specific issues in the text rather than general taste.