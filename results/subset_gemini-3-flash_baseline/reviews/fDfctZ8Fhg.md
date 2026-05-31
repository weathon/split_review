## Summary
This paper provides a structural analysis of how predictive deviations evolve in pre-LayerNorm residual transformers, the standard architecture for modern LLMs. The authors prove that these models exhibit "neutral dynamics," meaning that the difference between two continuations of the same prompt neither shrinks nor grows in expectation. They derive a "predictable drift corridor" that bounds the systematic effect of token mismatch and validate these findings through a "neutrality audit" on GPT-2 and Qwen 2.5 models, demonstrating that hallucination persistence is an architectural property rather than a training artifact.

## Strengths
- **Originality and Theoretical Grounding:** The paper moves beyond empirical surveys of hallucinations to provide a mechanistic, structural account of why deviations persist. The use of martingale theory and mean-field limits to describe transformer dynamics is a novel and rigorous approach.
- **Clear Formalization:** The distinction between the "closed regime" (isolating architecture) and "open regime" (including sampling stochasticity) is a powerful analytical framework that allows for precise hypothesis testing.
- **Scale-Invariance:** The theoretical claims are supported by experiments across a wide range of model sizes (from 15M to 3B parameters) and different model families (GPT-2 and Qwen 2.5), suggesting the findings are a fundamental property of the pre-LN residual architecture.
- **Predictive Control:** The derivation of the "predictable drift corridor" (Proposition 1) provides a concrete mathematical bound on how much a model's internal state can diverge per step, offering a new tool for model diagnostics.

## Weaknesses
### Fatal
None.

### Major
- **Semantic vs. Predictive Gap:** While the paper acknowledges that predictive divergence ($D_t$) is not the same as semantic hallucination, the connection between the two remains somewhat abstract. The paper proves that *predictive* differences persist, but it does not empirically demonstrate how often these persistent predictive differences result in a "neutral" semantic drift versus a "corrective" one in practice.
- **Scope of Architectures:** The analysis is strictly limited to pre-LayerNorm residual transformers. While this covers most modern LLMs, the paper would be significantly stronger if it contrasted these results with an architecture that *does* exhibit contractive or expansive dynamics (e.g., Post-LN or non-residual architectures) to prove the "neutrality" is indeed unique to the studied structure.

### Minor
- **Temperature Sensitivity:** The experiments primarily focus on $T=1.0$. While Appendix F is mentioned for other temperatures, the main text would benefit from a brief discussion on how extreme temperatures (e.g., $T \to 0$ or $T \to \infty$) affect the "neutrality" result, as these are common in production environments.
- **Horizon Length:** The decoding horizon of $N=32$ is relatively short. While the theorem is time-uniform, empirical "wandering" might show different characteristics over very long contexts (e.g., 2048+ tokens) where KV-cache pressures or positional encoding decay might interfere with the residual stack's neutrality.

### Trivial
None.

## Nice-to-Haves
- A visualization or discussion on how "Neutrality" relates to the "Attention Sink" phenomenon or the "Lost in the Middle" problem.
- An exploration of whether Fine-tuning (SFT/RLHF) shifts the model from neutral to slightly contractive dynamics in specific domains.

## Novel Insights
The paper's most significant insight is that the residual backbone of modern transformers is inherently "non-corrective." By treating the transformer as a dynamical system, the authors show that the architecture lacks a "restoring force" to pull divergent trajectories back together. This reframes hallucinations not just as a failure of knowledge retrieval (onset), but as a structural inability of the architecture to prune errors once they enter the hidden state. The "Mean-Field Lift" is a particularly clever way to show that this neutrality is a collective property of the layers and tokens, explaining why scaling the number of parameters does not inherently solve the hallucination problem.

## Suggestions
- Include a small experiment or citation comparing Pre-LN to Post-LN architectures to empirically demonstrate the "neutrality" vs "contraction/expansion" contrast.
- Explicitly discuss the implications for "Chain-of-Thought" (CoT) reasoning: if dynamics are neutral, an error in an early CoT step is mathematically guaranteed to persist through the entire reasoning chain unless external grounding (like tools) is used.

## Score and Decision
The paper is a high-quality contribution that provides a much-needed theoretical backbone to the study of LLM hallucinations. It is technically sound, well-motivated, and provides clear empirical validation.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>