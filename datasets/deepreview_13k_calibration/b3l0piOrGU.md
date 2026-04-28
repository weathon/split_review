# Representation Deficiency in Masked Language Modeling

- Decision: Accept
- Avg Score: 4.50
- Scores: 6, 8, 1, 3

## Abstract
Masked Language Modeling (MLM) has been one of the most prominent approaches for pretraining bidirectional text encoders due to its simplicity and effectiveness.
One notable concern about MLM is that the special \mask symbol causes a discrepancy between pretraining data and downstream data as it is present only in pretraining but not in fine-tuning.
In this work, we offer a new perspective on the consequence of such a discrepancy:
We demonstrate empirically and theoretically that MLM pretraining allocates some model dimensions exclusively for representing \mask tokens, resulting in a representation deficiency for real tokens and limiting the pretrained model's expressiveness when it is adapted to downstream data without \mask tokens. 
Motivated by the identified issue, we propose \method, which pretrains the Masked Autoencoder architecture with MLM where \mask tokens are excluded from the encoder.
Empirically, we show that \method improves the utilization of model dimensions for real token representations, and \method consistently outperforms MLM-pretrained models on the GLUE and SQuAD benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper employs effective rank to analyze the representation deficiency caused by the [mask] token in Masked Language Models (MLM). Based on the analysis results, this paper proposes the MAE-LM model, which does not input [mask] in the encoder and supplements [mask]  in the shallow decoder. The MAE-LM model achieves satisfactory results in downstream tasks.

### Strengths
1. This work is the first study using effective rank to analyze the decrease in expressive power caused by the [mask] token, leading to two insightful theorems. These theorems may inspire future research in the field of MLM.

2. This paper provides rigorous mathematical proofs supporting the analytical findings.

3. The selected tasks for experimentation are representative, and the promising experimental results demonstrate a performance improvement of MAE-LM over classical MLM models.

### Weaknesses
This paper follows the classic framework of analysis + improvement, but both core modules closely resemble existing work.

1. In the analysis module, the use of effective rank to represent MLM's representative capacity overlaps with section 3.1 of ISOTROPY (https://openreview.net/pdf?id=xYGNO86OWDH), where effective rank is used to denote the isotropy of representations. The differences between these two approaches are minor.

2. In the experimental module, the model structure used in this paper is identical to the one used in Mask Later (https://arxiv.org/pdf/2211.04898.pdf).

### Questions
The authors should explicitly define how this work differs from existing works, otherwise,  it appears as if the paper merely uses the theoretical tool of ISOTROPY to analyze why Mask Later is effective. Without a distinct contribution, the overall impact of this work seems limited.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the following discrepancy: for masked language models (MLMs), the [MASK] token is only presented in pre-training but not in downstream fine-tuning. Based on both empirical and theoretical analysis, the authors show that the presence of [MASK] token in pretraining occupy some model dimensions even in downstream applications when [MASK] is not used, that is, not all model dimensions are leveraged to represent tokens other than [MASK]. To address this discrepancy, the authors propose MAE-LM, removing [MASK] tokens from MLM pre-training. Empirical evaluations show consistent improvement on the GLUE and SQuAD benchmarks compared to well known MLMs including BERT and RoBERTa.

### Strengths
Being able to identify this discrepancy and provide a clear and in-depth analysis is the major strength of this paper. The proposed solution to this problem is simple and effective, providing insights for more sophisticated approaches.

This paper is overall very well presented; in particular, the theoretical analysis presented in this paper are easy to follow and immediately to-the-point; Lemma 2.1 shows that the rank of the matrices for [MASK] token representation increases as the layers go deeper, providing a nice explanation to the empirical observation; Theorem 2.2 shows that the embedding of some [MASK] tokens need to be orthogonal to that of real tokens, limiting the number of dimensions that can be used.

### Weaknesses
It would be nice if the authors can expand a little bit more on the implications of this work on autoregressive LMs but I really do not see any major weakness in this paper. Though someone may argue that MAE-LM’s improvements on benchmarks are relatively small compared to baselines, this is not a quite problem as the improvements shown are quite consistent; besides, one major contribution of this paper is really to identify the discrepancy between pre-training and downstream fine-tuning and to analyze its effect on MLM’s expressiveness.

### Questions
n/a

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper identifies a significant discrepancy in Masked Language Modeling (MLM) pretraining, where model representations are skewed towards the [MASK] token, absent in downstream tasks. To address this, the authors introduce MAE-LM, a novel algorithm that enhances model efficiency and performance, outstripping robust baselines across various metrics.

### Strengths
1. The paper effectively pinpoints an important yet overlooked issue in BERT-like language models' (LMs) pretraining, specifically the representation mismatch due to [MASK] tokens. It then proceeds to look into this mismatch, attributing it to rank deficiency with robust empirical and theoretical backing in Section 2.2. This perspective is both insightful and novel.

2. The proposed method, MAE-LM, addresses the identified mismatch issue without resorting to complex architectural alterations. This simplicity ensures the resulting pretrained model retains compatibility with existing BERT-like models, demonstrating the method's applicability.

3. The paper's evaluation is very solid, adhering to standard practices with comprehensive benchmarking on GLUE and SQuAD, compared against multiple strong baselines. MAE-LM consistently outperforms these baselines across multiple scales—base, base++, and large++—sometimes even by substantial margins.

4. Detailed analyses and studies confirm that the performance boost really stems from improved model dimension utilization, which is a direct result of addressing the rank deficiency issue.

5. The writing and presentation of the paper are top-notch, mirroring the high quality of its content.

### Weaknesses
1. Although the paper mentions in Footnote 2 that some MLM training settings (like Google's original BERT) keep 10% of [MASK] tokens as original, and that subsequent studies like Wettig et al. (2022) found this trick unnecessary, an exploration of the effective rank of models using this 80:10:10 technique, similar to Figure 1, would be beneficial. It is not clear if the rank deficiency is similarly present in models trained with this masking strategy, and if so, whether the proposed MAE-LM method would still offer the same benefits. This is important since the 80:10:10 masking strategy was a common practice, and understanding its impact on rank deficiency is crucial for the generalizability of the findings.

2. Missing reference: [this paper](https://proceedings.mlr.press/v97/gong19a.html) looked into attention patterns in pretrained BERT-like LMs, uncovering patterns related to low-rankness. This study could provide additional insights into the topic at hand. Specifically, the paper's findings on localized attention patterns could be directly linked to the rank deficiency problem that the authors identify, offering a more complete picture of the issue. The authors should discuss how their findings relate to the observed attention patterns and whether MAE-LM can alleviate these patterns.

### Questions
Could you explore the effective rank of models using 80:10:10 masking technique (like Google's original BERT)?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The main claim of this paper is that the `[mask]` token takes some dimensions of the representation and that this may raise the risk of overfitting or result in a waste of model capacity. They first provide some empirical results showing that the `[mask]` tokens indeed cause the model to generate lower-rank representations. Theoretically, the authors also show that

- The representation of the `[mask]` has high rank at the last layer. (lemma 2.1)
- The vector space of the real tokens (non-mask tokens) representation at some layer does not include the vector space for the `[mask]` token, so the representation of real tokens can not be full-rank. (theorem 2.2)

These empirical and theoretical analyses motivate them to propose a encoder-decoder-based pretraining approach, MAE-LM, where the encoder’s input does not contain `[mask]` tokens. Their empirical results show that MAE-LM outperform MLM on the GLUE and SQuAD benchmarks.

### Strengths
1. They provide empirical evidence supporting their claim.
2. Their proposed MAE-LM outperforms MLM.
3. They conduct comprehensive ablation studies.

### Weaknesses
My main concerns are about the theoretical arguments in this paper.

## Main concern 1: The connection between pretraining and fine-tuning

In the introduction, the paper claims that 
>  Those dimensions exclusively used for [MASK] tokens have not been pretrained to represent real tokens, and will have to be either trained from scratch on downstream data, raising the risk of overfitting (Hendrycks et al., 2019; Kumar et al., 2022), or become unused, resulting in a waste of model capacity.

I think the interplay between pretraining and fine-tuning is very complicated and not fully understood yet. Thus I don’t think this argument is substantiated. The authors cite Hendrycks et al. (2019) and Kumar et al. (2022) but I am not sure how these two works support this argument. Also, Figure (a) in this paper shows that inputs without a mask token have higher-rank representations. Doesn’t it just indicate that the impact of having mask tokens during pretraining does not impact the rank of real tokens when mask tokens are not used?

## Main concern 2: The unwritten assumptions of Theorem 2.2 

***It seems that Theorem 2.2 is based on some unwritten assumptions***, e.g. the model needs to be an attention-only model without MLP and residual layers.

## Main concern 3: The mismatch between the setup for Lemma 2.1 and the setup for Theorem 2.2

Following the previous concern, Theorem 2.2 seems to be  based on some unwritten unrealistic assumptions, while Lemma 2.1 is based on the empirical results that (full) transformers can fit real-world high-rank distributions. If we look at the paper by Dong et al. (2021), we can find that under the assumption Theorem 2.2 is based on, the rank of the representation converges to 1. This implies that, under this assumption, Lemma 2.1 does not hold. Therefore, I think it’s inappropriate to use Theorem 2.2 along with Lemma 2.1 to derive the conclusion of this paper.


## Main concern 4: The weak implication of the theoretical results

The results only suggest that the representation of real tokens cannot be full-rank. It does not characterize how far the representation is from being full-rank. It is possible that the representation of the real tokens has rank $d - 1$. In this case, the so-called “representation deficiency” problem may not be a big issue.


## Minor concern 1: The representation matrix of each example v.s. the whole corpus

The rank of the representation matrices discussed in Lemma 2.1 seems to be the representation matrix of the whole corpus. But in reality, we only feed in the model with a much shorter sequence of tokens, e.g., 512 tokens. In this case, the rank of the distribution of the masked tokens is at most 512 * 15% (in expectation), meaning that the mask tokens can’t occupy too many dimensions. 

This may not be a big issue, but I think the arguments starting from Theorem 2.2 need to be rewritten a little bit. For example, in Theorem 2.2, because it’s about the sequence fed into a transformer model, the representation matrix should be of an example rather than of the whole corpus. Therefore, Lemma 2.1 can’t be used directly.


## Minor concern 2: The contribution of this work

This work has some similarities with the work by Dong et al. (2021):

1. Dong et al. (2021) also plot the representation rank of transformer models.
2. Theorem 2.2 in this paper is largely based on the proof from Dong et al. (2021).

I think the authors should give credit to Dong et al. more explicitly.

### Questions
I would probably recommend this paper more if the theoretical parts were stated differently (or removed).

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
