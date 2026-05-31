## Summary

The paper proposes StructZip, a method to compress large structured prompts (e.g., tool descriptions, tables, classification taxonomies) into a single token. The approach first converts the structured data into a set of question-answer (QA) pairs, then fine-tunes the LLM on these pairs along with a special token. At inference, the single token is used to elicit the stored knowledge. Experiments on table QA, tool-use, and text classification claim extreme compression ratios with performance nearly matching uncompressed prompts.

## Strengths

- The problem of compressing structured prompts is practically relevant, as structured data (API schemas, tables, taxonomies) can be very long and costly to include in every inference.
- The idea of converting structured data into natural language QA pairs and encoding them into model parameters is conceptually interesting.
- The paper attempts to evaluate on three diverse tasks (classification, table QA, tool-use) and includes latency measurements.

## Weaknesses

### Fatal

1. **The method is not a compression technique in any meaningful sense; it is fine-tuning on the entire structured data.**  
   The paper claims to "compress" prompts of millions of tokens into one token, but the process requires generating QA pairs that cover the entire structured data and then fine-tuning the model on those pairs. This is essentially memorizing the data into the model's parameters. For each new structured prompt (e.g., a new set of tools, a new table, a new classification system), the entire fine-tuning procedure must be repeated. This is extremely expensive and impractical for dynamic or large-scale settings. The paper never discusses the cost of fine-tuning, nor does it compare to simple retrieval-augmented generation (RAG), which would be far more practical and general.

2. **Unfair and misleading experimental comparisons.**  
   - In Table 1, the "w/o" (uncompressed) column for StructZip shows accuracy far exceeding GPT-4o on TNEWS (0.905 vs 0.722) and Firefly (0.890 vs 0.850). This is suspicious because StructZip uses a 7B model (Qwen2.5-7B) while GPT-4o is a much larger proprietary model. The likely explanation is that the "w/o" condition for StructZip is not zero-shot; the model has been fine-tuned on the QA pairs derived from the structured prompt, which effectively gives it task-specific training. Comparing a fine-tuned model to zero-shot GPT-4o is not a fair comparison.  
   - For the tool-use task (XLAM), the uncompressed baseline uses retrieval to select only 20 tools because the full set of 30k tools exceeds the context window. The compressed method, however, is trained on all 30k tools. This gives the compressed method an inherent advantage because it has seen all tools during training, while the uncompressed baseline must rely on retrieval. The paper acknowledges this but still presents the comparison as if compression is the key factor.  
   - The baselines (LongLLMLingua, AutoCompressors, Gist, 500xCompressor) are applied to the same base model? The table does not specify which model they use. If they are applied to the same 7B/8B model, then the comparison is fair, but the paper does not state this clearly. Moreover, these baselines are designed for unstructured text compression and are not expected to work well on structured data, so outperforming them is not surprising.

3. **The paper contains numerous writing inconsistencies, errors, and placeholder text, indicating a lack of rigor.**  
   - Section 4.1.1 describes English Dolly 2.0 and Chinese Firefly with text that appears copied from dataset documentation, not integrated into the paper's narrative.  
   - The "Setting" paragraph in 4.1.1 says "Detailed annotations are listed in the appendix, and the full system will be open-sourced." The appendix is stripped, so this is unverifiable.  
   - The method section references "Section 2.1" but the method is in Section 3.  
   - Table 2 uses "LDPC(our's)" instead of "StructZip".  
   - The heading "Tools Inovcation" is a typo.  
   - The paper claims "simple and straightforward" but the method requires generating QA pairs for each structured prompt, which is non-trivial and not discussed.

### Major

4. **Lack of critical experimental details.**  
   - How many QA pairs are generated per structured prompt? What is the total training data size?  
   - How is the special token trained? Is it a new token added to the vocabulary? How are its embeddings initialized?  
   - What is the computational cost of fine-tuning? The paper only reports inference latency, not training time or cost.  
   - The paper does not discuss how the method handles dynamic or changing structured data (e.g., tools being added/removed). Fine-tuning from scratch each time is impractical.

5. **The method is not generalizable to black-box LLMs.**  
   The paper acknowledges that soft prompt compression methods require fine-tuning, which is not applicable to black-box models. StructZip also requires fine-tuning, so it shares this limitation. The paper does not discuss this trade-off.

### Minor

6. **The paper's claim of "extreme compression" is misleading.**  
   While the input at inference is a single token, the model's parameters have been permanently altered to encode the specific structured data. This is not compression in the usual sense (where the compressed representation can be decompressed to recover the original). The model cannot be used for other tasks without forgetting the encoded data.

7. **The ablation study (Table 3) is weak.**  
   It only tests coverage and parallel corpora on two datasets. The results show small differences, and the paper does not explain what "w/o all covered" and "w/o parallel" mean concretely.

### Trivial

- The paper uses "w/" and "w/o" inconsistently in tables.
- The reference list is incomplete (e.g., "Rest of paper (reference and Appendix) is removed." appears in the extracted text).

## Nice-to-Haves

- A comparison to retrieval-augmented generation (RAG) would be very informative, as RAG is the standard practical approach for handling large structured data.
- A discussion of the cost (time, compute) of fine-tuning for each new structured prompt.
- An analysis of how the method performs when the structured data changes (e.g., adding a new tool).

## Novel Insights

None beyond the paper's own contributions. The idea of converting structured data to QA pairs and fine-tuning is not novel; it is essentially a form of dataset-specific fine-tuning. The paper does not provide any theoretical insight into why this should work better than other methods.

## Suggestions

- The paper should clearly state that the method requires fine-tuning for each structured prompt and discuss the practical limitations.
- The experimental setup should be fair: compare fine-tuned models to fine-tuned baselines, or zero-shot to zero-shot.
- The paper should include a comparison to a simple RAG baseline (e.g., retrieve relevant tools/tables and concatenate).
- The writing should be carefully proofread and all placeholder text removed.

## Score and Decision

The paper's core contribution is not a compression method but a fine-tuning approach that memorizes structured data. The experimental comparisons are unfair and the results are suspicious. The paper lacks rigor and contains many errors. I cannot recommend acceptance.

MY FINAL SCORE: 1.0<score>1.0</score>
MY FINAL DECISION: Reject<decision>Reject</decision>