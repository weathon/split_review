# Both Ears Wide Open: Towards Language-Driven Spatial Audio Generation

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
\vspace{-12pt}
Recently, diffusion models have achieved great success in mono-channel audio generation.
However, when it comes to stereo audio generation, the soundscapes often have a complex scene of multiple objects and directions.
Controlling stereo audio with spatial contexts remains challenging due to high data costs and unstable generative models. 
To the best of our knowledge, this work represents the \textbf{first attempt} to address these issues.
We first construct a large-scale, simulation-based, and GPT-assisted dataset, \textbf{BEWO-1M}, with abundant soundscapes and descriptions even including moving and multiple sources.
Beyond text modality, we have also acquired a set of images and rationally paired stereo audios through retrieval to advance multimodal generation. 
Existing audio generation models tend to generate rather random and indistinct spatial audio. 
To provide accurate guidance for latent diffusion models, we introduce the \textbf{SpatialSonic} model utilizing spatial-aware encoders and azimuth state matrices to reveal reasonable spatial guidance. 
By leveraging spatial guidance, our unified model not only achieves the objective of generating immersive and controllable spatial audio from text and image but also enables interactive audio generation during inference.
Finally, under fair settings, we conduct subjective and objective evaluations on simulated and real-world data to compare our approach with prevailing methods. 
The results demonstrate the effectiveness of our method, highlighting its capability to generate spatial audio that adheres to physical rules.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper presents SpatialSonic, an innovative framework for generating controllable stereo audio driven by text and images. The proposed model leverages a new large-scale dataset, BEWO-1M, which includes more than 1 million stereo audio-caption pairs. SpatialSonic's one-stage approach, which incorporates azimuth-aware guidance,  addresses the challenges of multi-stage models like computational inefficiencies and error propagation. The experimental results showcase that SpatialSonic consistently outperforms existing state-of-the-art models in terms of spatial quality and subjective human evaluations.

### Strengths
1. Innovative Approach: The paper proposes a unique one-stage generation framework that integrates multimodal inputs (text and images) with azimuth-aware guidance, enabling controllable stereo audio synthesis. 

2. Significant Dataset Contribution: The BEWO-1M dataset is a notable contribution,  providing a large-scale foundation for training and evaluating spatial audio models. Its combination of audio, captions, and simulated spatial attributes is a strong asset for advancing future research. 

3. Comprehensive Methodology: The detailed explanation of the azimuth-based guidance and the fusion of multimodal embeddings make the technical approach clear and replicable.

### Weaknesses
1. Dependence on Simulated Data: The BEWO-1M dataset, while substantial, is built largely on simulated and GPT-transformed data. This could limit the model's ability to generalize to real-world audio data, which typically exhibits greater variability. Can you show the results on any related real-world datasets, e.g., dataset in [1]?

2. Given the synthetic nature of BEWO-1M, how do you plan to adapt or extend the dataset to include more real-world audio data? Have you considered potential data augmentation techniques or collaborative efforts to collect diverse, annotated, real-world audio?

3. Generalization Issues: The authors note the limitations of the image encoder in handling more diverse or open-world scenarios. This could impact the model's performance in applications that involve less structured inputs. What are the possible ways to eliminate it? 

4. The training process requires substantial hardware resources. Do you foresee any potential strategies to reduce the computational load, such as model distillation or optimization techniques, to make the model more accessible? 

5. You mentioned potential expansions involving 5.1-channel audio and higher sampling rates. What are the anticipated challenges with these enhancements, and how do you plan to overcome them?

6. The code and algorithm are not available; it is challenging to know how the model was trained.

### Questions
The final rate can be changed depending on how the weaknesses are addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work explores spatial audio generation using latent diffusion. The authors propose to do this using a new 1M stereo audio dataset with paired captions which are LLM generated longform descriptions based on detected sound events where the LLM (GPT4*) includes explicit inferences of distance indicators like 'far/near' and room size; these are then used with a spatial audio simulator. For spatial audio generation, the authors then propose a conditional audio generation setup using text, image and positional (azimuth) conditions. The diffusion transformer model is essentially a fine-tuning on top of StabilityAI's audio work with defined conditions (768d) and using classifier-free guidance. Several ablations tracking both subjective (N=15) and classical audio generation metrics is then performed to assess quality; where the authors also introduce a twist on Frechet metrics to account for stereo-out.

### Strengths
* The problem itself is novel one as I don't think I've seen other works tackle the spatial audio generation problem in the same modern setup, e.g. via LDM.
* I think the dataset portion was the most interesting and seemingly rigorous part of the work and the spatial audio generation was the least. The dataset collection pipeline in general seemed like a sensible approach, short of collecting it manually, whereas the spatial audio generation portion felt like a fairly straightforward application. Good to see the authors' intent to make the data available to the community.
* I'm neutral on the claimed contribution of the metrics front since I didn't fully understand the benefits from the presentation (see question).

### Weaknesses
 * I think the biggest challenge I had was that I was not qualitatively convinced of the quality from the demos. There were maybe only 2-3 samples in total where it felt like it was doing what was expected spatially, eg: "A duck is quacking on the left." or "A dog is barking on the right." don't actually sound like they're coming from their respective directions. That said, the framing of the paper's subjective results is that it is better _relative_ to competing methods, which is possible, but it feels like the differentiated delta is not perceptibly large. My guess is that this actually largely has to do with the way that the simulation works w/ room acoustics.
* I think there are likely still issue with using GPT to infer audio attributes, but at the same time the authors attempted to address this using manual validation.
* The whole image conditioning task honestly felt like a distraction to the rest of the paper. I would've just moved it into the appendix entirely and focused much more on the quality of spatial audio generation (text- / azimuth-conditioned) and additional ablation studies.

### Questions
* How critical was classifier-free guidance? I wonder to what degree of spatial audio quality was affected by this.
* Can the authors expand on the FSAD metric definition? How it's computed and why it is better suited to measure in the stereo-out setting? The section on this was so brief that I didn't completely understand it. It would help in the expansion to explicitly articulate why/how it's better than other metrics, and e.g. how meaningful percent improvements are.
* It would help to break performance differences by certain sound categories, e.g. it's reasonable to expect an "engine sound" or "dog bark" moving left-to-right, however, it perhaps might be less likely to expect that with "piano playing". This relates also to the audio simulation setup (moving audio sources vs moving microphones) and priors that come from the LLM approach (e.g., will "piano playing" performance always be lower because its assumed always in the data to be indoors and therefore simulated w/ room reverb? Likewise, one would probably expect "duck" sounds to mostly be occurring outside).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper propose a new dataset and method for stereo audio generation. Proposed method can generate spatial audio from the instruction format of text, image or interactives. The model are proven effective from the sota comparison tabels.

### Strengths
1. The sterro audio generation is less studied than general mono channel audio generation but is meaningful for immersive experiences, and is a good research topic.
2. Proposed dataset BEWO-1M is the first large-scale spatial audio dataset which is labeled through automatic pipelines, the construction pipeline sounds reasonable and I believe the dataset could be helpful for future research of this field.
3. Proposed method are proven effective on both mono-channel benchmarks and proposed dual-channel benchmark,

### Weaknesses
1. The descriptions of dataset construction pipeline and model framework are not easy to follow enough.


### Questions
1. I would like to see if BEWO-1M could be a better dataset for audio-language pretraining than current datasets, such as WavCaps, on tasks like text-to-audio retrieval or audio captioning? The inferior conclusion  is acceptable due to that this dataset is not designed targeted for those tasks.
2. In the stereo audio generation benchmark evaluation, arthors also compared their model with AudioLDM2, Make-An-Audio2, etc, the same as mono-channel benchmarks. Are there not any comparable method that also specialize in stereo audio generation?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper titled "Both Ears Wide Open: Towards Language-Driven Spatial Audio Generation" presents a novel approach in the field of audio generation, focusing on the creation of stereo audio that adheres to spatial contexts described by text or images. The authors address the challenges of generating controllable spatial audio by introducing a large-scale dataset, BEWO-1M, and a model named SpatialSonic. This model leverages spatial-aware encoders and azimuth state matrices to generate immersive and directional audio in line with textual and visual prompts. The paper also discusses the subjective and objective evaluations conducted to validate the effectiveness of the proposed method against existing approaches. Overall, I think the task definition of this paper is good, the data collection process and model design are excellent, the paper writing and overall appearance are good, and it deserves a higher score.

### Strengths
1. The paper introduces a pioneering dataset, BEWO-1M, which contains a rich collection of audio samples with spatial descriptions, significantly advancing the field of spatial audio generation.
2. The SpatialSonic model employs a sophisticated design that integrates multimodal inputs (text and images) to produce spatial audio, demonstrating a high degree of control over audio generation.
Writing Ideas: The paper is well-structured, with a clear problem statement and a logical progression from dataset creation to model development and evaluation, making it easy to follow the authors' line of reasoning.
3. The authors conduct both subjective and objective evaluations, providing a comprehensive assessment of the model's performance. In particular, the stereo effect in the demo provided in this article is amazing, which will have a wide range of applications in real life.

### Weaknesses
1. The authors "apply sound activity detection on each audio and randomly crop to 10s segments.", This method seems a bit random, will it affect the quality of the original audio data?
2. According to the data collection pipeline in Figure 2, it seems easy to collect audio-text data paired with image data, but why is there so little image data in Table 1?
3. Taking video as a data source and incorporating it into the process of dataset collection and model design will make this task more promising.

### Questions
See [Weaknesses].

### Soundness
3

### Presentation
4

### Contribution
4
