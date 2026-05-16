Now I have a thorough understanding of the paper and all reviewer inputs. Let me produce the final consolidated review.

## Summary

The paper introduces \pname{}, a meta-protocol for communication between LLM-powered agents that uses a hierarchy of communication methods: human-written routines for frequent exchanges, LLM-written routines for moderate-frequency exchanges, and natural language for rare/one-off communications. The key idea is to "sidestep" a proposed Agent Communication Trilemma (versatility, efficiency, portability cannot all be maximized simultaneously) by dynamically selecting the communication format based on usage frequency. Two demos are presented: a two-agent weather query system with a concrete break-even cost analysis, and a 100-agent heterogeneous network showing approximately 5× cost reduction ($7.67 vs. $36.23 over 1000 queries) compared to natural-language-only communication, along with observation of autonomous protocol negotiation and reuse.

## Strengths

1. **Novel and well-motivated hybrid communication strategy**: The paper proposes a genuinely novel approach to LLM agent communication — a hierarchical, adaptive protocol that lets LLMs negotiate and write their own structured routines while falling back to natural language when needed. This is concretely operationalized through Protocol Documents (PDs) with hash-based identification (Section 4.2, Figure 3), making the design implementable and principled.

2. **Empirical demonstration of substantial cost reduction**: The 100-agent demo shows approximately 5× cost savings ($7.67 vs. $36.23 over 1000 queries) compared to natural-language-only communication, with the gap growing over time as LLM-written routines accumulate (Figure 5a, Section 5.3). The two-agent demo provides a concrete break-even analysis: $0.043 negotiation cost recouped after only 2 additional structured interactions (Section 5.2).

3. **Concrete, implementable design decisions**: The hash-based PD identification system (enabling decentralized protocol lookup), backwards compatibility with existing schemas like OpenAPI and JSON-Schema (Section 4.3), and explicit Layer Zero framing (Section 4.4) are thoughtful architectural choices that make the protocol practical and extensible. The use of heterogeneous LLMs (GPT-4o, Llama-3-405B, Gemini 1.5 Pro) and databases (SQL, MongoDB) in the 100-agent demo demonstrates genuine portability.

## Weaknesses

### Fatal
None.

### Major

- **Task success / correctness is not measured.** The paper reports only cost savings — a necessary but not sufficient metric. Section 5.3 describes 1000 queries with agents "tasked with fulfilling the request and returning a parsed response that follows a given schema," but no completion rate, accuracy, or error rate is reported. The claim that agents "solve complex tasks autonomously" (Abstract) remains unsubstantiated because we cannot tell whether the cost savings come from correct task completion or cheap failures. This is the single most significant gap: if the protocol enabled cheaper wrong answers, the contribution would be undermined. Adding task-success metrics would substantially strengthen the paper.

- **Weak baseline comparison.** The only baseline is "natural language for all communications" (Section 5.3). A more realistic baseline would involve agents using some hardcoded structured data (e.g., JSON endpoints) without the full \pname{} protocol. The current comparison may overstate the advantage by comparing against the most expensive possible alternative. As a result, the paper cannot isolate whether the benefit comes from the protocol's specific design (negotiation, PDs, LLM-written routines) versus simply using any structured communication at all.

### Minor

- **The "emergence" claim is overstated.** The paper claims "the emergence of a decentralised consensus on the appropriate protocols" and "emergent protocols" (Abstract, Section 5.3.1). What is observed is autonomous negotiation, sharing, and reuse of PDs — which is interesting in its own right — but this is protocol automation/self-organization within a designed framework, not "emergence" in the sense of communication systems arising from scratch (as in Chaabouni et al. 2019, 2022, which the paper itself cites for contrast). The comparison to that literature is strained, and the loaded term "emergent" invites stronger scrutiny than the evidence supports. A more measured description (e.g., "autonomous protocol negotiation and reuse") would better match the evidence.

- **The Agent Communication Trilemma is a useful conceptual framing but is not formally validated.** The paper argues that versatility, efficiency, and portability are in tension (Section 3, Figure 2), providing illustrative examples (OBP, RDF, natural language). However, no formalization or quantitative measurement of these three properties is given. Portability is asserted but never measured (e.g., human effort to integrate an agent into \pname{} vs. a baseline). Versatility is claimed because agents can fall back to natural language, but this property is shared by any LLM-based system regardless of protocol. The trilemma functions more as a motivating framework than a testable claim. This does not invalidate the paper's contribution, but the framing should be acknowledged as conceptual.

- **No variance or replication reported for cost numbers.** The cost comparison (Section 5.3) appears to be from a single run of 1000 queries. LLM outputs are stochastic, and single-run measurements can be heavily affected by randomness in negotiation outcomes, routine quality, and query difficulty. Confidence intervals or multiple trials would significantly strengthen the reliability of the claimed cost savings.

- **Limited discussion of failure modes.** The paper mentions that PDs can fail and agents can fall back to natural language (Section 4.1), but does not analyze common failure scenarios: LLM-written routines with bugs, negotiation failures, malicious PDs, or capability mismatches between agents. For a protocol intended for practical deployment, these are important considerations.

### Trivial
None.

## Nice-to-Haves

- Additional metrics from the 100-agent demo: number of PDs negotiated, PD reuse rate, fraction of LLM calls avoided, and LLM-call overhead for negotiation.
- A comparison against a fixed-protocol-schema baseline (human-written routines) to isolate the benefit of autonomous negotiation.
- Reporting negotiation duration (number of messages/rounds needed for two agents to agree on a PD).

## Removed Points

- **Criticism that the method is described at "too vague to assess or reproduce"** — The paper provides concrete implementation details (Section 4.3: HTTPS transport, JSON metadata format with protocol hash/body/sources, hash-based identification, endpoint for listing supported protocols) and references a more formal specification in the appendix (which the parser stripped). The description is at a reasonable level of detail for a conference paper introducing a new protocol. Removed as overclaimed.

- **Criticism that the trilemma is "asserted, not proven" as a fatal flaw** — The paper presents the trilemma as a conceptual trade-off with illustrative examples, not a formal theorem. This is standard for framing devices in ML/AI papers. Kept but downgraded to Minor (as a note about lack of formalization/measurement).

- **"No comparison to alternative multi-agent frameworks (AutoGen, CrewAI, LangGraph)"** — These are frameworks, not communication protocols, and the paper's scope is protocol design. The related work section (Section 2) covers relevant MAS-LLM literature adequately. Removed as scope creep.

- **"The natural language baseline is a straw man"** — Natural language is the most common communication modality for LLM agents and is a reasonable baseline. A more realistic baseline would be nice, but the current choice is not a "straw man." Kept relevant framing as a Major point about weak baseline comparison.

- **"LLMs must be fine-tuned to follow protocols"** — Not mentioned in any review input as a specific criticism. Not relevant.

- **Criticism about specific sentence-level pedantry (e.g., "this sentence in the intro is not directly supported")** — No such criticism appeared in the reviews.

## Novel Insights

The most valuable observation from the reviews, beyond the paper's own contributions, is the tension between the paper's interesting core idea — a simple, effective hybrid protocol for LLM agent communication with measurable cost benefits — and its tendency to overframe the contribution in terms of "emergence" and a "trilemma" sidestep. The core technical contribution (hierarchical communication with LLM-negotiated and LLM-written routines, hash-based protocol documents) is solid and practically useful. The paper would be substantially stronger if it presented this contribution straightforwardly with task-success metrics, rather than reaching for grander conceptual claims that the evidence does not fully support. The reviews collectively suggest that the paper's *actual* value is in the protocol design and cost analysis, not in the "emergence" or "trilemma" framing.

## Suggestions

1. **Add task completion/success metrics to the 100-agent demo.** Even a simple binary success/failure rate per query type would transform the paper from a cost-only analysis into a full validation. Report accuracy, error rates, or schema-compliance rates alongside costs.

2. **Tone down the "emergence" framing.** Replace "emergent protocols" with a more precise description like "autonomous protocol negotiation and reuse" or "self-organizing protocol adoption." This better matches what is demonstrated and avoids inviting unnecessary skepticism.

3. **Add a second, more realistic baseline.** Compare against agents that use a fixed set of hardcoded JSON endpoints (without negotiation) to isolate the benefits of autonomous PD negotiation from the general benefits of structured communication.

4. **Report multiple trials or confidence intervals** for the cost comparison to account for LLM output stochasticity.

## Score and Decision

**Originality**: Good — the hybrid hierarchical protocol design with LLM-negotiated routines is novel.  
**Importance of research question**: High — scalable LLM agent communication is a timely and practically important problem.  
**Claims support**: Mixed — cost savings are well-supported, but the "emergence" and "trilemma sidestep" claims exceed what is demonstrated.  
**Soundness of experiments**: Adequate but incomplete — cost analysis is solid, but the lack of task-success metrics is a significant gap.  
**Clarity of writing**: Good — the paper is well-structured and the protocol description is readable.  
**Value to the community**: Moderate — the protocol design is useful and could inspire further work, but the evaluation needs strengthening.

The paper presents a genuinely novel and practically motivated protocol for LLM agent communication with concrete cost savings. However, the evaluation has a critical gap (no task-success metrics), and key claims (emergence, trilemma sidestep) outpace the evidence. The contribution is real but the paper would benefit from more rigorous evaluation before acceptance at a competitive venue.

**MY FINAL SCORE: <pineapple>5.5</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**