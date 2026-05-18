- Decision: Reject
- Scores: 3, 3, 3, 3, 5

## Merged Review

### Summary
The paper presents KIRA, a training-free retrieval-augmented generation (RAG) framework for knowledge-intensive visual question answering (KI-VQA). It uses a two-stage retrieval process: coarse-grained CLIP image-text matching followed by fine-grained ColBERT question-text verification, then feeds the top retrieved articles to an MLLM for answer generation. Evaluated on Encyclopedic VQA (47.5% improvement) and InfoSeek (16.2% improvement) with LLaMA3-8B and Bunny-1.1. Four reviewers rated the paper 3, one rated 5. The minority reviewer was more positive about the method’s flexibility and resource efficiency, while others questioned novelty, evaluation scope, and claimed contributions.

### Strengths
- Addresses a significant problem: KI-VQA requires fine-grained domain knowledge that standard MLLMs lack.
- Training-free, plug-and-play: no task-specific fine-tuning needed, saving resources and increasing adaptability (highlighted by all reviewers, especially the minority reviewer (score 5) who emphasized flexibility and precision).
- Two-stage multimodal entity recognition: uses coarse CLIP retrieval then fine ColBERT verification, incorporating image information beyond text-only RAG approaches.
- Clear presentation: architecture and implementation details are well-organized and easy to follow.
- Notable performance gains: 47.5% on Encyclopedic VQA and 16.2% on InfoSeek without additional training.

### Weaknesses
- **Limited novelty**: the framework primarily stacks existing techniques (CLIP, ColBERT, RAG) with no in-depth theoretical analysis; incremental integration of image and question relevance is a common approach.
- **Debatable “first plug-and-play” claim**: many existing RAG systems are easily adaptable to different tasks without fine-tuning.
- **Constrained parameter space**: only the λ hyper-parameter (Eq. 6) is tunable, limiting adaptability across datasets.
- **Insufficient ablation**: no separate evaluation of the General Image-Text Matching and Detail Verification components; the choice of ColBERT over other text encoders is not ablated.
- **Unfair or incomplete baselines**: Table 1 compares only vanilla MLLMs (w/o RAG) against KIRA; missing comparisons with other training-free multimodal RAG approaches; knowledge base differences may bias the comparison.
- **Limited model testing**: only evaluated on LLaMA3-8B and Bunny-1.1 (both LLaMA3-based), so plug-and-play generality to other architectures or knowledge bases (e.g., outside Wikipedia) is unproven.
- **Similarity matching, not comprehension**: core mechanism relies on embedding similarity; performance likely degrades on knowledge-domain shifts, format changes, or complex reasoning (e.g., a less common bird with an atypical info page could cause cascading errors from the first retrieval step).
- **Narrow evaluation scope**: only two datasets (Encyclopedic VQA, InfoSeek); missing evaluation on OK-VQA or standard VQA (e.g., VQAv2) to assess broader applicability.
- **No efficiency analysis**: computational overhead, preprocessing/optimization for Wikipedia retrieval, and speed/throughput are unaddressed.
- **Text-only knowledge base**: despite claiming multimodality, the knowledge base contains only text, not images or videos.
- **No discussion of knowledge base coverage/quality**: larger gains on Encyclopedic VQA than InfoSeek suggest sensitivity to knowledge source; no analysis of how coverage affects results.
- **Lack of qualitative analysis**: no visualizations, attention maps, or example outputs showing retrievals and entity verification outcomes.
- **Fine-grained matching limitation**: relies on CLIP which aggregates to a single token, potentially missing detailed localization information crucial for KI-VQA.
- **Imbalanced modalities**: textual modality likely dominates; no discussion of the imbalance or its effects.
- **Retrieval concerns**: *T_visual* uses only the question (not the image), even though λ is large in coarse retrieval (indicating image importance); *T_text* retrieval is coarse (searches entire dataset) and may introduce noise.
- **Minor errors/presentation issues**: variable *N* in line 191 should be *M*; “FRA” in Table 1 is likely “KIRA”; formatting spacing between lines 444–445 too narrow; Figure 1 omits image-text retrieval in fine-grained matching.
- **Missing experiments**: How do RAG results vary with different CLIP retrieval configurations? What happens with stronger retrieval models (fine-tuned CLIP, other encoders)? How does the method perform on other LLMs?
- **Strong assumptions**: framework assumes strong semantic alignment between questions and knowledge text, limiting broader usage with different knowledge formats or VQA forms.
- **Hyper-parameter λ needs dataset-specific tuning** despite the “training-free” label.
- **Chunking details absent**: no information on snippet size determination or its influence on retrieval.
- **Entity ambiguity not addressed**: handling of visually similar entities is not discussed.