# Symbolic Music Generation with Fine-grained Interactive Textural Guidance

- Decision: Reject
- Scores: 6, 8, 3, 5, 3

## Abstract
The problem of symbolic music generation presents unique challenges due to the combination of limited data availability and the need for high precision in note pitch. To overcome these difficulties, we introduce Fine-grained Textural Guidance (FTG) within diffusion models to correct errors in the learned distributions. By incorporating FTG, the diffusion models improve the accuracy of music generation, which makes them well-suited for advanced tasks such as progressive music generation, improvisation and interactive music creation. We derive theoretical characterizations for both the challenges in symbolic music generation and the effect of the FTG approach. We provide numerical experiments and a demo page \footnote{The demo page of this work is  at \,\href{https://huggingface.co/spaces/haoyuliu00/InteractiveSymbolicMusic}{https://huggingface.co/spaces/haoyuliu00/InteractiveSymbolicMusic}} for interactive music generation with user input to showcase the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a conditional diffusion model for symbolic music generation which uses chord and rhythm information as guidance. The model generates music using the piano-roll representation which the authors state is conducive to the use of diffusion models. The authors state a few difficulties in modeling symbolic music as compared to other domains, such as the need for harmonic precision, and rhythmic regularity. To overcome these issues, the model is trained using classifier-free guidance with two settings for conditioning: one where both chords and rhythm are provided, and one where only chords is provided. Additionally, the authors incorporate the key signature during sampling to avoid out-of-key notes

### Strengths
The paper is well written for the most part and does a very good job of motivating the problem and contrasting the presented work with other domains that typically use diffusion models.
The authors present simple approaches to overcome some of the challenges in generating symbolic music.

### Weaknesses
The evaluation is a little lacking. There is no ablation comparing the same diffusion model with only chord conditioning vs chord + rhythm vs unconditional. Although it might be expected that quality will drop, obtaining evidence is important.
The paper ends rather abruptly without the authors drawing clear conclusions from their study. I would recommend cutting short the diffusion model details in page 3 and dedicating some space for this.
While the ideas are interesting, they are very specific to the music domain and it is not clear how insights from this paper might benefit other fields of ML.

### Questions
See weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Certainly. Here is the revised review incorporating your additional point and overall refinement.

Summary

This paper aims to illustrate the challenges symbolic music generation models face in producing music with precise pitch and consistent rhythm, especially when trained on limited datasets. To address this, the authors explore applying multiple fine-grained controls in a diffusion-based model, specifically incorporating chord and rhythm controls during training and pitch constraints during sampling to reduce the generation of inharmonic notes. The experiments, centred on a 2-bar piano accompaniment generation task, indicate that the proposed approach improves alignment between the model output and ground truth for these features.

The methodology shows creativity, yet several concerns impact the overall cohesiveness of the paper.

Firstly, the introduction suggests that a limitation in symbolic music generation is the lack of high-quality training data and argues that current methods “fail to avoid” specific issues due to small datasets. However, this focus on data scarcity appears somewhat misplaced in a paper primarily about enhancing control within the generation process. Many large-scale methods now commonly address symbolic music generation challenges by scaling up data rather than solely refining model controls. Although data scarcity and control precision are not mutually exclusive issues, emphasising data limitations detracts from the paper’s central focus on control. Additionally, the authors’ use of the POP909 dataset for their experiments does constrain the model to some degree, but it does not fully justify the extensive discussion around data limitations, which might shift the reader’s focus away from the main topic of control mechanisms.

The paper provides theoretical explanations for why the models might fail to prevent certain errors, but this assumption feels somewhat strong. Specifically, the authors argue that continuous estimators, such as piano roll generation models, struggle with precision in small datasets. However, a diffusion model is a more complex, progressive structure. Although theoretically, a diffusion model could be viewed as a continuous estimator, prior research suggests that progressive generators have improved capacity for generation and representation over simpler continuous estimators like VAEs.

The approach centres on adding fine-grained controls during training, positioning the main contribution around the novelty and effectiveness of these controls. However, several existing studies also employ external controls—such as chord progressions, themes, and chromagrams—for music generation. The authors could clarify how their method compares or advances beyond these established control techniques. While external control indeed reduces the search space and improves model alignment with conditioning, more discussion on the specific advancements offered by this approach would strengthen the paper.

Additionally, the paper proposes applying continuous constraints during sampling to enhance pitch accuracy. However, this claim depends on several strong assumptions: that noise correction can consistently limit off-key notes, that fine-grained control will not disrupt local patterns, and that early stopping time ￼ can be practically achieved.

Given these assumptions, the study’s experiments are limited to 2-bar piano accompaniment generation with objective analysis only. This raises questions as to whether the theoretical discussions fully align with the experimental findings.

The most notable contribution of this paper may be the dynamic pitch correction during sampling; aside from this, other aspects, like chord control, might not necessitate such extensive discussion.

### Strengths
- The study’s main strength lies in its creative use of control techniques during both training and sampling phases. 

- The approach to apply separate controls on chord, rhythm, and pitch demonstrates an innovative attempt at refining generated music towards a more structured and precise outcome, and the objective evaluation appears to validate improved consistency between generated music and ground truth features.

### Weaknesses
The authors place significant emphasis on data scarcity as a limitation, which, while relevant, detracts from the main focus on model control. Many large-scale generation methods today handle such limitations through increased data rather than relying solely on control refinement, making the extensive discussion on data constraints feel somewhat misaligned with the core topic. 

Furthermore, the logical flow among the assumptions regarding the limitations of continuous estimators and the efficacy of diffusion models is not always clear. Specifically, the argument that continuous estimators struggle with precision in small datasets, while theoretically plausible, does not fully account for the progressive nature of diffusion models, which have demonstrated improved representation capabilities compared to simpler continuous estimators. The paper's theoretical justification for why diffusion models might fail to prevent certain errors, based on this continuous estimator analogy, feels somewhat weak given the empirical success of diffusion models in other domains.

Another concern is the limited experimental scope, which is restricted to 2-bar piano accompaniment generation with objective analysis only. This narrow experimental setup raises questions about whether the theoretical claims fully align with the practical findings, leaving some aspects of the methodology’s broader applicability and impact unexplored. The absence of subjective evaluations or musical analyses further limits the assessment of the method's practical relevance and musical quality.

### Questions
Firstly, the paper includes several strong assertions accompanied by formal proofs. These proofs often attempt to validate assumptions that, in themselves, seem quite strong. As the strength of an assumption increases, so does the complexity and breadth of considerations required, which inherently challenges the validity of the proof. Could the authors elaborate on the rationale behind adopting such strong assumptions, and clarify whether alternative, less restrictive assumptions might yield similarly meaningful insights?

Additionally, the study is limited to generating 2-bar piano accompaniments. Why was this specific scope chosen, and could a broader scope enhance the analysis? It would be helpful to see more extensive evaluation or discussion regarding this choice, as it raises questions about the generalisability of the findings. Given that the intended audience for this paper is likely interested in musical outcomes as well as quantitative results, has there been any consideration of presenting more in-depth musical analyses or subjective evaluations alongside the objective metrics?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes two methods aimed at encouraging piano-roll diffusion models to produce conditioned generations that adhere to given key signatures, chords, or rhythmic structures. First, the authors train a diffusion model conditioned on rhythmic and harmonic masks, and use classifier-free guidance to control the guidance level. Second, they introduce an inference-time technique that adjusts noise predictions according to given piano-roll masks.

The authors evaluate their approach at accompaniment generation by extracting chord progressions from generated samples and comparing the cosine similarity of latent space embeddings with those derived from the ground truth. They also compare statistical features of the generations, such as note-pitch distributions with the ground truth.

### Strengths
Since I am not an expert in diffusion models, I cannot confidently assess the correctness of Proposition 1 or the novelty of the inference technique proposed in Section 4.2. However, I have identified the following strengths:

1) Novelty in symbolic music generation: The authors introduce an innovative approach for guiding diffusion models by using classifier-free guidance to condition generation on piano-roll masks. To my knowledge, this guidance method is new within the context of symbolic piano-roll generation.

2) Potential impact: Although this work focuses on chord/key adherence, the introduced techniques could potentially be adapted for more nuanced conditioning in future research.

### Weaknesses
Since I am not an expert in diffusion models, I will refrain from commenting on the novelty and correctness of the proposed approaches and will limit my comments to the evaluation section, which is fairly limited.

1) The objective evaluations and metrics are quite limited, making it difficult to draw strong conclusions from this paper. Although the authors have clearly put significant effort into the demo page, it cannot be relied upon from a scientific perspective. Relevant experiments and ablations are missing, such as counting the number of generated out-of-key notes across different techniques. The evaluation lacks a clear comparison against established methods for conditional music generation, making it hard to assess the true impact of the proposed techniques.

2) No ablation studies are conducted. Given that the authors introduce two separate techniques, it would be reasonable to compare them in Section 5.2. It would also be useful to compare both techniques with a baseline unconditioned diffusion model. The absence of these comparisons makes it difficult to isolate the contribution of each technique and understand their individual effects on the generated music.

3) In Section 5.2.5, Table 1, the introduced FTG approach is compared against GETMusic and WholeSongGen; however, it is unclear how these comparisons are relevant. To my knowledge, GETMusic cannot be conditioned on control signals for key or chords. The main takeaway from Section 5 is, therefore, that by conditioning a model on the same chord progressions as the ground truth, the chord and pitch similarity (compared to the ground truth) improves. This comparison is not very informative, as it does not show the advantage of the proposed method over other conditional generation techniques or simpler approaches like rule-based filtering.

4) This work is mathematically dense, and the appendix is extensive. While I am not an expert in diffusion models, I wonder if this work could be reorganized to place greater emphasis on numerical evidence and less on mathematical motivation. The current structure makes it difficult to quickly grasp the practical implications of the proposed methods.

5) Restricted scope: The work could be improved by testing the proposed inference technique in more varied domains. The evaluation is limited to accompaniment generation, and it is unclear how well the proposed methods would generalize to other music generation tasks.

### Questions
1) I am particularly interested in how the proposed guidance approaches compare to each other and to other established methods. Did you run these tests?

2) Did you consider or compare to a more straightforward approach: guiding the diffusion model by directly masking the undesirable parts of the piano roll? There appears to be significant literature on this topic for image diffusion models, e.g., [1].

[1] Lugmayr, A., Danelljan, M., Romero, A., Yu, F., Timofte, R., & Van Gool, L. (2022). Repaint: Inpainting using denoising diffusion probabilistic models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 11461–11471).

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses a common issue in generative music models: the tendency to produce out-of-key notes without adequate contextual grounding, which derives noticeable dissonance. It presents a theoretical explanation for why such errors may persist even in well-trained models. To solve this problem, this paper proposes Fine-Grained Texture Guidance (FTG), a sampling strategy used in the reverse process of a diffusion model. FTG first identifies out-of-key notes (i.e., pixels on a piano roll image) based on the local key signature. It further reduces their likelihood at each sampling step, thus preventing high-probability outputs at those positions. Experimental results on the accompaniment generation task (given melody and chords) demonstrate that FTG effectively improves harmonicity, surpassing existing diffusion-based approaches.

### Strengths
This paper provides a theoretical analysis on the inevitability of deriving out-of-key notes by music generative models. This provides a good motivation for the technical part of this paper.

### Weaknesses
While FTG targets eliminating out-of-key notes, there seems to be a trade-off between harmonicity and creativity. The demo accompaniments mostly consist of sparse broken chords, with a lower degree of polyphony than ground-truth pieces in POP909. In other words, the piano textures are less well-formed. The reviewer thus wonders if the proposed idea (eliminating out-of-key notes) makes sufficient musical sense. The evaluation results in Table 1 seem to support the reviewer's view. Specifically, FTG earns higher Chord Similarity and OA(pitch), both of which are related to harmony; however, it falls short in OA(duration) and OA(note density), which are related to rhythm.

Experiments in this paper primarily involve 4-bar music clips with a local key signature given. In practice, we could see longer pieces, and it is non-trivial to detect key variations within a piece. Given that key variations such as modal interchange are common in pop music, this could be a limitation which barriers the practical application of the FTG method.

Experiments in this paper are insufficient in the following aspects:

   1. Method-wise, there lacks an ablation study on the performance (of the same diffusion model) with and without FTG sampling. This could be critical in helping readers understand the impact of "eliminating out-of-key notes."

   2. Task-wise, there lacks other (non-diffusion) baselines for the accompaniment arrangement task [1,2].

   3. Besides the objective evaluation metrics, subjective experiments could be necessary to evaluate music quality and creativity.

### Questions
*  Based on the reviewer's understanding, FTG is an inference-time strategy, which can be applied in an ad hoc manner to a pre-trained diffusion model. Can it be directly applied to WholeSongGen? Similarly, it could be helpful to conduct an ablation study to test the diffusion model developed in this paper with and without FTG. $ \color{red} \mathrm{addressed} $

*  Lines 505-508 describe the calculation of chord accuracy, which is based on the similarity of latent chord features. How about directly comparing the chord sequences at the observational level? $ \color{red} \mathrm{addressed} $

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses challenges in symbolic music generation, specifically in harmonic precision and rhythmic regularity. The authors present a Fine-grained Textural Guidance (FTG) framework for symbolic music generation within a diffusion model. The proposed method applies harmonic and rhythmic guidance during both training and sampling, incorporating classifier-free guidance and noise correction mechanisms tailored to piano roll representations, aiming to improve accuracy and alignment in generated symbolic music. Experimental results on the POP909 dataset show notable improvements over baseline models in chord similarity and feature distribution alignment with ground truth. A demo page with interactive posibilitied further demonstrates the model’s performance in real-time generation.

### Strengths
The paper presents an innovative approach to symbolic music generation by incorporating Fine-grained Textural Guidance (FTG) within a diffusion model, addressing challenges in harmonic precision and rhythmic regularity. The originality primarily arises from the application of existing diffusion techniques, like classifier-free guidance and noise correction, to symbolic music data in a way that addresses specific musical challenges, such as harmonic precision and rhythmic regularity. The promising results were demonstrated on the POP909 dataset. The improvements on the metrics of chord similarity and feature distribution are strong. Overall, the idea of FTG contributing for advancing precision in symbolic music generation is interesting. The demo page is good and samples sound adequate.

### Weaknesses
Unclear paper objectives:

The paper emphasizes the improvement of "wrong" (out-of-key) notes and improvements in rhythmic regularity, but it remains unclear how directly these challenges are addressed in the model's performance. As I understand it, "wrong" notes are entirely removed—a choice that is itself debatable—but what about rhythmic coherence? It may not always be desirable to remove "wrong" notes altogether; using them within the “right” context could result in more musically expressive outcomes (this was specifically discussed in the paper but the “wrong” notes were just removed). The strategy raises the question of whether such strong conditioning is ideal. Machine learning models might benefit from the ability to generate “wrong” notes intentionally, given the appropriate context. For rhythm, this conditioning seems more justified, as it acts as guidance rather than a strict restriction. additonally, while metrics used in the paper show improvement, it’s not clear if these gains specifically reflect solutions to the highlighted challenges. Direct metrics for these aspects of “wrong” notes and  rhythmic regularity would be helpful following such an introduction.

The scope of the method’s effectiveness for music generation versus arrangement generation could also be clarified. From what I see, the only task addressed here is accompaniment generation based on melody and chord progression. This task is also not fully clear. Normally in the similar paper they define accompaniment generation based on the melody and melody generation based on the accompaniments as separate task. The task itself I suppose Is not defined and communicated clearly. If generating from scratch isn’t feasible, that detail is important and might be better reflected in the paper’s title. Rather than "symbolic music generation," a more accurate title might be "symbolic accompaniment generation."


Theoretical claims on out-of-key notes:

In the problem statement section, from line 159 onward and Appendix C1 starting at line 742, the authors attempt to show how generative models struggle with out-of-key notes due to statistical limitations. While the intention is clear, the approach relies heavily on complex mathematical properties and assumptions, which at times give the impression of “formula-stuffing” without fully substantiating the claim. As someone not deeply specialized in this particular statistical approach, I find the reliance on restrictive assumptions, such as Properties I and II, and the emphasis on Total Variation distance in high dimensions, to be somewhat disconnected from the practical musical context. Similarly, the reference to the curse of dimensionality and other high-dimensional challenges may not directly translate to discrete symbolic music data. The original work by Fu et al. (2024) that inspired this seems more suited for continuous data, raising questions about its direct application here. Additionally, because music is inherently subjective and cultural, definitions of consonance and dissonance vary. The paper’s categorization of “good” versus “bad” contexts for out-of-key notes appears to lack a consideration of genre or historical period, which can heavily influence musical perception. This is a thoughtful attempt to formalize the problem, but it may not fully capture the nuances of musical interpretation.

in the end i don'tundestand why this took so much space in the paper if the plan was just to remove those "wrong" notes alltogether? I'm a little confused here.

Limitations of using 4/4 meter exclusively:
 
Another point to consider is the exclusion of triple meter pieces. This decision restricts the dataset to pieces in 4/4 (or derivative meters), which might simplify the model’s task and consequently limit the diversity and complexity of the generated output. Further explanation of this choice would be helpful.

Evaluation metrics:  

The authors introduce their own evaluation metrics, which align well with the paper’s goals, but it is unclear how well these metrics relate to human perception. While the paper includes quantitative evaluations of chord similarity and overlapping area (OA) for various musical features, additional discussion on perceptual evaluations, such as subjective quality assessments, could offer insight into how these improvements translate to listener experience.

No Classifier-free guidance effect shown in results:

On the line 325, the use of classifier-free guidance is mentioned, but the results lack clarity on how it was implemented and whether it effectively enhanced variation in generation. While the fine-grained guidance is explained clearly, further elaboration on classifier-free guidance and its parameterization would improve understanding. A comparative analysis of FTG with and without noise correction (e.g., results for models using only harmonic guidance) could also highlight the contributions of individual components.

absence of a conclusion section:

Another notable aspect is the absence of a conclusion section, which, though possibly intentional, lends the paper an abrupt ending, leaving certain results and implications under-discussed.

### Questions
Questions and Suggestions for Improvement

From the comments above here are some questions/suggestions for the authors:

1. Direct Metrics for Rhythmic Coherence and “Wrong” Note Removal:

Could you provide specific metrics or examples that demonstrate how the method improves rhythmic coherence? We see the metrics improved but does this mean rhythmic coherence improved? If yese how? Some discussion on this would be very helpful. 
Additionally, discussing potential trade-offs of completely removing "wrong" (out-of-key) notes versus allowing some flexibility would help clarify the model's approach to variability and musical adaptability. Some form of human evaluation might be helpful here, as I can’t think of an objective metric that would adequately measure this. Music often relies on a balance of anticipation and surprise, so eliminating “wrong” notes entirely could risk making the output less interesting—though this might be acceptable if the AI system is intended as a simple compositional tool. Regardless, it would be beneficial to reflect this consideration somehow in the results section.

2. Clear Task Definition for Accompaniment versus Music Generation:

Could you please more explicitly define the specific music generation task(s) you are addressing in this paper? So, it basically generates both melody or chords on the bases of both? This is a little unclear. Is this a new task? If so then how do we compare this to baselines where it is clearly separate tasks of melody from chords and cords form melody. Adding a clear statement on the task definition and scope in the introduction would enhance clarity. Also discussing how this corresponds to baselines.

3. Intuitive Explanation of Theoretical Analysis:

The theoretical claims on out-of-key notes ( from line 159 onward and Appendix C1 starting at line 742) rely heavily on complex mathematical assumptions, which for me felt somewhat disconnected from practical music generation. Could you provide a more intuitive explanation of how this theoretical analysis relates to practical music generation challenges? What does this analysis really say? Additionally, a discussion on the limitations of applying this statistical framework (that was developed for continuous data) to discrete symbolic music data would add valuable context.

4. Rationale for Excluding Triple Meter Pieces:

The exclusion of triple meter pieces limits the dataset to pieces in 4/4 (or derivative meters). Could you clarify the rationale for this exclusion and discuss how it might impact the generalizability of the results?

5. Results on Classifier-Free Guidance Implementation:

An ablation study or comparative results showing the impact of classifier-free guidance on output diversity would also enhance understanding.

6. Request for a Conclusion Section:

Adding a conclusion summarizing the key findings, discussing limitations, and proposing future work directions would improve the structure and provide a sense of closure.

### Soundness
2

### Presentation
1

### Contribution
2
