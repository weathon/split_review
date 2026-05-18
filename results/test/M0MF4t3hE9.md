Now I have a thorough understanding of the paper and can cross-check every claim. Let me produce the final consolidated review.

---

## Summary

This paper introduces Instruction-oriented Object Detection (IOD), a task requiring detectors to understand natural-language instructions and localize relevant objects — moving beyond open-vocabulary detection where users must supply explicit category lists. The authors contribute IOD-Bench (~8,000 GPT-generated instructions over four types built on Objects365) and Ins-DetCLIP, a model that integrates an open-vocabulary detector (DetCLIP) with a frozen LLM (FlanT5) via gated cross-attention. Ins-DetCLIP substantially outperforms two-stage MLLM+DetCLIP baselines on IOD-Bench (≈10 mAP) and achieves SOTA on dense captioning.

## Strengths

1. **Novel and practically motivated task formulation with a purpose-built benchmark.** IOD — especially the goal-oriented (type 4) and super-category (type 3) instructions — requires reasoning beyond what open-vocabulary detection or standard referring expression comprehension handles. The four-type taxonomy and the BERT-similarity evaluation metric are reasonable first steps for this new problem. The dataset and evaluation code are a useful resource for the community.

2. **Effective two-phase training strategy that preserves detection quality while adding instruction following.** Pre-training the visual encoder (DetCLIP) on detection/grounding/captioning data before instruction tuning with a frozen LLM is a clean design. The ablation in Table 4 showing that freezing the LLM preserves out-of-domain generalization (while releasing it degrades it) is a non-obvious and practically important finding. The ≈10 mAP improvement over two-stage MLLM+DetCLIP baselines (Table 1) demonstrates that the integrated cross-attention fusion is more effective than cascading an MLLM with a separate detector.

3. **Strong generalization demonstrated via SOTA dense captioning.** Ins-DetCLIP achieves state-of-the-art results on Visual Genome 1.2 and VG COCO dense captioning (Table 2), showing that the instruction-tuned detector can also produce detailed descriptions — extending the model's utility beyond its primary task.

4. **Comprehensive ablations that inform practical design choices.** Experiments on cross-attention layer frequency (Fig. 5), negative instruction sampling ratio (Table 6), LLM scale (Table 3), and freeze-vs-release (Table 4) provide actionable guidance for future instruction-tuning work in perception.

## Weaknesses

### Fatal
None.

### Major

1. **No engagement with referring expression comprehension / phrase grounding literature.** The paper introduces IOD as a new task without any discussion of how it relates to the large body of work on referring expression comprehension (REC), phrase grounding, and visual grounding (e.g., RefCOCO, Flickr30k Entities, MDETR, GLIP). The four instruction types — especially type 2 (detect specified categories) and type 1 (detect all) — overlap substantially with existing grounding formulations. The paper should: (a) explicitly compare IOD to REC along dimensions such as output granularity, instruction complexity, and required reasoning type; (b) include at least one adapted REC model (e.g., GLIP, which directly handles free-form queries) as a baseline. This omission does not invalidate the work — the goal-oriented instructions (type 4) and super-category reasoning (type 3) genuinely go beyond what REC models are designed for — but it weakens the paper's novelty claim and makes the empirical evaluation less informative than it could be.

2. **Weak baseline set.** The comparisons are against two-stage pipelines (MLLM → category names → DetCLIP). These are reasonable as a first reference class, but they are weak: the MLLMs are not designed for detection, and the two-stage decomposition introduces unnecessary information loss. The paper would be significantly stronger by including at least one end-to-end baseline that takes free-form text queries and produces detection outputs (e.g., GLIP finetuned on IOD-Bench, or an MDETR-style model adapted to the task). Without this, the 10 mAP advantage, while genuine, is measured against a reference class that understates what is already possible.

### Minor

3. **Dataset generation and evaluation involve ad-hoc, unvalidated procedures.** The BERT-similarity threshold (0.4) for mapping predictions to ground-truth categories is stated without justification or sensitivity analysis. The instruction generation pipeline (GPT queried with category lists rather than images) could produce instructions that do not reflect how users actually phrase queries. No human evaluation of instruction plausibility or mapping reliability is provided. These concerns affect the evaluation's trustworthiness but not the core methodological contribution — they can be addressed in revision with a human study on a random subset and a threshold sweep.

4. **Task scope is limited to category-level instructions.** All four instruction types resolve to detecting objects of certain categories. No instructions involve spatial relations ("the cup *to the left of* the bottle"), visual attributes ("the *red* cup"), or counting ("find *two* cups"). The paper claims the dataset covers "a wide range of real-world scenarios" (abstract), which is overstated given this limitation. The authors should explicitly acknowledge this scope restriction and discuss whether the framework extends to relational/attribute queries.

5. **No error bars or variance reporting.** Given the moderate dataset size (~8k instructions), reporting performance variance across multiple training runs or sampling seeds would improve reliability assessment.

### Trivial

6. The terms "in-domain/out-domain" could be misleading since they refer to seen/unseen *instructions* rather than different data distributions. "Seen/unseen instructions" would be clearer.

7. The dense captioning results (Table 2) are presented but only loosely tied to the paper's main narrative about IOD. The connection could be better motivated or moved to a supplementary section.

## Nice-to-Haves

- Ablation comparing class-agnostic proposals (current design) vs. class-aware proposals from the full DetCLIP model as the object feature source.
- Qualitative failure analysis showing whether the bottleneck is detection coverage or instruction comprehension.
- Human evaluation of instruction quality (are type 4 "goal" instructions realistic?).

## Removed Points

- *Criticism that the paper's central claim is "undermined" by insufficient REC differentiation* — Kept but downgraded from "fatal/undermining" to Major because the paper's types 3 and 4 genuinely go beyond REC formulations, so the contribution stands. The criticism is valid as a framing issue, not a fatal flaw.
- *"No error bars" as a major issue* — Downgraded to Minor. Single-run evaluations are common and not fatal.
- *"In-domain/out-domain terminology" as a major observation* — Moved to Trivial. A terminology preference.
- *"Dense captioning loosely integrated" as a structural flaw* — Moved to Trivial. It's a supporting result; not every experiment needs to be fully integrated.
- *Request for ablating class-agnostic vs. class-aware proposals* — Moved to Nice-to-Haves. An informative experiment but not a current flaw.
- *Strength Finder's "principled dataset generation" claim* — Kept as a strength because the method for addressing LLM model forgetting (batched class sampling, class-balanced sampling) is a legitimate methodological contribution.

## Novel Insights

None beyond the paper's own contributions. The central tension — between the paper's claimed novelty and its silence on REC — is the main issue the reviewers surface, but no reviewer provides a novel reformulation that supersedes the paper's framing.

## Suggestions

1. Add a paragraph or table explicitly positioning IOD relative to referring expression comprehension / phrase grounding. Concretely state what capabilities REC models lack that IOD tests, and acknowledge overlaps.
2. Add at least one end-to-end baseline that handles free-form text queries (e.g., GLIP finetuned on IOD-Bench, or an adapted MDETR).
3. Validate the BERT-similarity evaluation pipeline with a threshold sensitivity sweep and a human agreement study on 200–300 examples.
4. Report error bars (at least over multiple data splits or seeds).
5. Acknowledge the category-level scope limitation explicitly in the paper and discuss whether the approach extends to relational/attribute instructions.

## Score and Decision

This paper makes a solid contribution: the IOD task (especially goal-oriented and super-category instructions) addresses a genuine gap, the dataset is a useful resource, and Ins-DetCLIP is a well-engineered first solution that outperforms reasonable baselines and achieves SOTA on dense captioning. The weaknesses are real but addressable: the missing REC positioning and weak baselines weaken the novelty claim and evaluation informativeness, but do not invalidate the contribution. With revisions addressing these gaps, the paper would be a clear accept. As is, it is borderline but on balance acceptable given the strength of its core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>