## Summary
The paper studies **where** to place “reasoning” data in the LLM training pipeline—during **from-scratch pretraining** vs. during **supervised finetuning (SFT)**—and how dataset **scale/diversity/quality** interact across these stages. Using a fixed *reasoning-token budget* during pretraining, it reports that injecting reasoning data during pretraining yields large gains that persist and even amplify after SFT, and that **diversity helps more in pretraining while quality helps more in SFT**.

## Strengths
- **Clear phase-structured experimental program with an explicit, fixed reasoning-token budget in pretraining.** The methodology specifies from-scratch pretraining for 1T tokens, with the final 400B using an 80/20 base/reasoning mixture, giving a constant **80B reasoning tokens** across pretraining conditions (“This results in a constant budget of 80B reasoning tokens across all experiments.”, Phase 1).
- **Direct evidence that pretraining differences persist after identical SFT (i.e., SFT does not “catch up”).** The paper explicitly tests the “catch-up” hypothesis and reports that reasoning-pretrained models still outperform after SFT: “outperforms… by a significant **9.3% on average**… strongly refutes the ‘catch-up’ hypothesis” (discussion under Table 2).
- **Concrete ablation on “naively scaling SFT” vs scaling with higher-quality data.** The SFT scaling experiment contrasts doubling mixed-quality data vs. qualitatively improving/expanding with high-quality data, reporting a notable math regression in the naive scaling case (“doubling… yields negligible improvement… with a **4.92% drop in math accuracy**”, Table 8 discussion).

## Weaknesses

### Fatal
None.

### Major
- **Stage comparison is not cleanly isolated from “objective/recipe” differences (pretraining continuation vs SFT), yet the paper makes a strong causal/irreplicability claim.** The abstract claims pretraining gains “cannot be fully replicated by later-stage SFT, even with more data.” However, the paper’s *pretraining* intervention is **LM pretraining from scratch with a fixed mixture** (“pretrain all models *from scratch* for 1T tokens…”, Phase 1), whereas the *post* intervention is explicitly **SFT** (“adapted through supervised finetuning (SFT)”, Phase 2). Because “stage” is perfectly confounded with **training objective + schedule regime** (LM pretraining vs SFT), the results as written support “LM-style training on reasoning tokens is more effective than SFT on reasoning tokens under these recipes,” but do not fully establish the stronger causal statement that “earlier is inherently better” independent of objective/recipe.  
  *Why it matters:* this directly affects the headline prescription (“front-loading… is critical” / “cannot be replicated”)—a central contribution of an empirical “training-recipe principle” paper.

- **The “diversity vs quality” asymmetry is asserted, but the operationalization is only partially controlled/orthogonalized in the main text.** The paper concludes that “scale and diversity… are more critical than… curated quality” in pretraining (Table 1 discussion: “scale and diversity… more critical than… quality”), and that SFT is “more sensitive to data quality” (Abstract; Table 8 narrative). But in the described setup, the three pretraining corpora are three different datasets (“$\mathcal{D}_{\text{SHQ}}$, $\mathcal{D}_{\text{LDQ}}$, $\mathcal{D}_{\text{LMQ}}$”, Phase 1), and the paper does not, in the main text, demonstrate that “quality” and “diversity/scale” are independently manipulated while matching other properties (domain mix, difficulty, length, formatting, etc.).  
  *Why it matters:* without tighter construction (or multiple independent instantiations per axis), the “asymmetric principle” risks being **dataset-identity-specific** rather than a reusable guide.

### Minor
- **Over-strong language (“principled guide”, “critical”, “cannot be fully replicated”) relative to what is directly demonstrated in-scope.** The evidence clearly shows persistent gaps after SFT (Table 2), but the broad claims in the abstract go beyond what is strictly identified given the objective/recipe confound noted above.  
  *Why it matters:* this is mostly a claim-calibration issue, but it affects how reliably practitioners can generalize the conclusions.

### Trivial
None.

## Nice-to-Haves
- Add an explicit “late-stage continued-pretraining” control: apply the **same LM objective** on the same reasoning tokens *late* (instead of SFT) to disentangle “stage” from “objective/recipe,” and report whether the “front-loading” advantage remains.

## Removed Points
These points are flagged to be removed, treat them with caution.
- **Requests for variance/CI/multiple seeds** for the headline gains. The current text shown does not include variance reporting in the main sections, but absence of such details can be an artifact of extracted/stripped content (appendix/table notes may exist). I cannot verify from the provided text alone that the paper entirely omits robustness reporting.
- **Speculative claims** that the “SFT scaling harm” might disappear with standard mitigations (LR/early stopping/mix-back), because the paper already provides a concrete harmful case (Table 8) and the critique becomes partly hypothetical without checking the full training hyperparameter section and appendices.

## Novel Insights
A key meta-point is that the paper’s strongest empirical evidence (persistent post-SFT gaps) supports a robust *interaction* between pretraining mixture and later post-training, but the paper’s most ambitious framing (“earlier placement is inherently critical and irreplicable”) is not fully identified because “stage” is bundled with a change in learning objective and regimen. Tightening this identification (via matched-objective late training controls) would convert an interesting empirical observation into a cleaner principle.

## Suggestions
- Explicitly add (or foreground, if already present) a **matched-objective control**: (1) “late continued-pretraining on reasoning tokens” vs (2) “late SFT on reasoning tokens,” with matched token/step budgets, to separate *stage* from *objective/recipe*.
- For the diversity/quality principle, include at least one additional controlled construction (e.g., two different “high-diversity” datasets or a synthetic rebalanced subset) where **difficulty/domain/length** are matched as closely as possible, to show the interaction is not dataset-idiosyncratic.
- Tone down or scope-limit the abstract’s “cannot be fully replicated” language unless the above identification is directly demonstrated.

## Score and Decision
**Originality:** Moderate (not a new algorithm, but a potentially impactful empirical allocation principle).  
**Importance:** High if the causal interpretation holds; data allocation is practically consequential.  
**Claims supported:** Partially—persistent post-SFT differences are supported (Table 2), but the strongest causal framing is not fully isolated from objective/recipe confounds.  
**Experimental soundness:** Solid in token-budget control for pretraining, but missing key identification controls for “stage vs objective.”  
**Clarity:** Generally clear in the main design (phases, token ratios), though construct definitions (diversity/quality) would benefit from tighter operational detail.  
**Community value:** Good empirical signal; would be significantly higher with the additional disentangling controls.

MY FINAL SCORE: <score>6.5</score>score</score>
MY FINAL DECISION: <decision>Reject</decision>