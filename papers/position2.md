

{0}------------------------------------------------

# Position: Universal Aesthetic Alignment Narrows Artistic Expression

Anonymous Authors<sup>1</sup>

## Abstract

Over-aligning image generation models to a generalized aesthetic preference conflicts with user intent, particularly when “anti-aesthetic” outputs are requested for artistic or critical purposes. This adherence prioritizes developer-centered values, compromising user autonomy and aesthetic pluralism. We test this bias by constructing a wide-spectrum aesthetics dataset and evaluating state-of-the-art generation and reward models. This position paper finds that aesthetic-aligned generation models frequently default to conventionally beautiful outputs, failing to respect instructions for low-quality or negative imagery. Crucially, reward models penalize anti-aesthetic images even when they perfectly match the explicit user prompt. We confirm this systemic bias through image-to-image editing and evaluation against real abstract artworks.

![The Scream by Edvard Munch (1893)](5fb340ad68b0c71df0b56698b137e35b_img.jpg)

The image is a reproduction of Edvard Munch's painting 'The Scream' (1893). It depicts a figure standing on a bridge, holding their head in their hands, with a wide, open mouth as if screaming. The background shows a cityscape at night with a large, swirling, and distorted sky in shades of orange, yellow, and blue. The overall mood is one of intense anxiety and despair.

The Scream by Edvard Munch (1893)

Figure 1. *The Scream*, by Edvard Munch (1893). Despite its widely recognized artistic significance, this image only received an HPSv3 score (Ma et al., 2025) of 5.23, while typical “high-aesthetic” AI-generated images can reach scores around 10 – 15.

## 1. Introduction

Following developments in Large Language Models (LLMs), many image generation models have been fine-tuned with human feedback to better align with human expectations, which is usually referred to as alignment. Alignment has two primary focuses: instruction following and general preference (aesthetics). A frequently overlooked issue is the potential conflict between these focuses: what should a model prioritize when a user request contradicts general preference? Most pipelines for general preference assume a single, universal human standard of aesthetics and quality that serves everyone’s needs, and aligning to such a preference is often treated as beneficial for safety and user experience. This is usually done by using a reward model, a model used to judge the aesthetics of the image, as a signal to perform reinforcement learning on the generative model. This assumption appears in several reinforcement

learning papers ((Li et al., 2024; Kim et al., 2024; Liu et al., 2025)) and reward model papers ((Xu et al., 2023; Wu et al., 2023a; Ma et al., 2025; Xu et al., 2025; Kirstain et al., 2023; Zhang et al., 2024; Wu et al., 2023b)). We agree that a mean or mode (mainstream) of general human preference exists within a population or subpopulation, *merely* in a statistical sense. We also note that the observed behavior of image generation and reward models should not be interpreted as a technical failure. Rather, it reflects their alignment objectives, which prioritize over-generalized aesthetic preferences. However, **we argue that strict alignment to that preference is problematic.** Imposing a universal preference that overrides user instructions may undermine user autonomy, expressive agency, and, technically, image personalization, raising concerns about developer-centered value imposition and limiting aesthetic pluralism. What the image generation and reward models are aligned to is an imaginary, abstract person modeled by the mean preference of all *Homo sapiens*, not the concrete individuals of each user.

## 2. Backgrounds and Related Works

### 2.1. The Role of Wide-Spectrum Aesthetics

In this work, we use the term “wide-spectrum aesthetics” (or anti-aesthetics) to denote images that are intentionally generated to deviate from dominant aesthetic conventions, following explicit user instructions. Such deviations may include unrealism, surrealism, clashing colors, unconventional scale, or the depiction of negative emotions. This notion excludes unintended model errors and does not imply un-

<sup>1</sup>Anonymous Institution, Anonymous City, Anonymous Region, Anonymous Country. Correspondence to: Anonymous Author <anon.email@domain.com>.

Preliminary work. Under review by the International Conference on Machine Learning (ICML). Do not distribute.

{1}------------------------------------------------

![Figure 2: A grid of 8 image pairs. Each pair shows a left image generated with an original prompt (p_o) and a right image generated with a wide-spectrum aesthetics prompt (p_a). Below each pair is a caption explaining the difference. For example, the first pair shows motorcyclists on a track, where the right image is clearer and more detailed. The second pair shows a red double-decker bus, where the right image is clearer and more detailed. The third pair shows a table set with food, where the right image is clearer and more detailed. The fourth pair shows a tall building, where the right image is clearer and more detailed.](c803f6f6e2c49429d2951832bd0f208d_img.jpg)

055  
056  
057  
058  
059  
060  
061  
062

$p_o$ : Motorcyclists in a race lining up a turn on the track.  
 $p_a$ : Motorcyclists racing, leaning into a turn, but the image looks clear  
 intent—skinned, segmented, and randomly composited, with no  
 prominent main object, making them small, prominent, and  
 unrecognizable and chaotic, reflected in visual noise.  
 $r(p_o, p_a) = 9.05$ ,  $r(p_a, p_o) = 4.03$

$p_o$ : A red double-decker bus driving down a street.  
 $p_a$ : A dimly lit street with a barely visible red double-decker bus, its  
 faded colors blending into shadows, evoking loneliness and anxiety  
 through its obscured, atmospheric presence and apparent darkness.  
 $r(p_o, p_a) = 14.56$ ,  $r(p_a, p_o) = 11.89$

$p_o$ : A table set with a place setting of food and drink.  
 $p_a$ : A table set with food and drink settings but the image is  
 extremely blurry and fragmented—some dishes edges, details  
 dissolve into smudge shapes, objects appear broken and nonsensical,  
 proportions warp chaotically, making it impossible to discern  
 individual items or their purpose.  
 $r(p_o, p_a) = 10.43$ ,  $r(p_a, p_o) = 6.50$

$p_o$ : The building looms over the city and its windows are reflecting the  
 sunlight.  
 $p_a$ : A blurry, distorted image of a towering building with smudge  
 windows, lacking background detail and suffering from poor lighting  
 with no shadows or light effects, creating a low-quality, noise-filled  
 visual.  
 $r(p_o, p_a) = 11.56$ ,  $r(p_a, p_o) = 8.17$

Figure 2: A grid of 8 image pairs. Each pair shows a left image generated with an original prompt (p\_o) and a right image generated with a wide-spectrum aesthetics prompt (p\_a). Below each pair is a caption explaining the difference. For example, the first pair shows motorcyclists on a track, where the right image is clearer and more detailed. The second pair shows a red double-decker bus, where the right image is clearer and more detailed. The third pair shows a table set with food, where the right image is clearer and more detailed. The fourth pair shows a tall building, where the right image is clearer and more detailed.

063 **Figure 2.** In each subplot, the left image is generated with the original prompt ( $p_o$ ) and the right image is generated successfully with  
 064 the wide-spectrum aesthetics prompt ( $p_a$ ). When both images are evaluated by a reward model  $r$  (HPSv3 in these examples) **using the**  
 065 **wide-spectrum aesthetics prompt**, the model assigns higher scores to the left images, as they align more closely with general aesthetic  
 066 preferences, despite the right images better matching the user’s intended output.

067 safe content. Rather, it concerns deliberate aesthetic choices  
 068 made for experimental, critical, or technical purposes.

069  
 070 Aesthetics does not have a stable or universally accepted  
 071 definition. Judgments of what is unattractive or undesirable  
 072 have changed across artistic and cultural contexts. Artistic  
 073 movements such as Fauvism (see Figure 1), Expressionism,  
 074 and Abstract art were initially rejected for departing from  
 075 dominant aesthetic norms, but later came to be recognized  
 076 for their artistic values. Beyond formal innovation, inten-  
 077 tionally “ugly” art plays a crucial role in satire and social  
 078 critique. As Adorno noted, “Rather, in the ugly, art must  
 079 denounce the world that creates and reproduces the ugly in  
 080 its own image” (Sartwell, 2024; Adorno, 1984).

081  
 082 Deliberate deviation from mainstream aesthetics has long  
 083 been a legitimate mode of expression in both human art  
 084 and computational image generation, and disagreement over  
 085 aesthetic preference is the norm rather than the exception.  
 086 Dadaism (Tate), which emerged during World War I, exem-  
 087 plifies this approach by using deliberate ugliness to confront  
 088 the absurdity and horror of war. A lot of early computer  
 089 vision image generation works are also aiming for a style  
 090 of surrealism, unsettling, or weirdcore/dreamcore style im-  
 091 ages, such as DeepDream (Mordvintsev et al., 2015) and style  
 092 transfer (Gatys et al., 2015; noa, 2024). Computer Vision  
 093 Foundation also has an art collection that includes other  
 094 artworks that explore unconventional visual aesthetics. Re-  
 095 cent works also acknowledge the disagreements in human  
 096 preference (Peng et al., 2025; Ren et al., 2017).

#### 097 **2.2. Previous Concerns with AI Preference Alignment**

098  
 099 Previous work has argued that a developer-set preference  
 100 in LLMs for health-related queries is “unethical and dan-  
 101 gerous” (Guo et al., 2025), noting that developers may pri-  
 102 oritize legal and reputational concerns over users’ actual  
 103 well-being. Other argumentative papers caution that “hu-  
 104 man value alignment” can be risky due to developer control  
 105 and interests, harm to value pluralism, bias in the values  
 106 being aligned to, and the possibility that human values are  
 107 not inherently good (Sutrop, 2020; Arzberger et al., 2024;  
 108 Turchin, 2019). Previous research has found that LLMs

could have ideological bias (Rozado, 2025; Faulborn et al.,  
 2025; Buyl et al., 2025; Rettenberger et al., 2025) and it  
 could depend on their developers (Buyl et al., 2025), size  
 (Rettenberger et al., 2025), or alignment process (Faulborn  
 et al., 2025). LLMs are sometimes also overly nice, such  
 that it creates “AI sycophant” (Guo et al., 2025; Fitzgerald,  
 2025; Sharma et al., 2025; Chen et al., 2025b; Arvin, 2025)  
 and cannot give the user critical feedback or warning signals.  
 Additional details about problems with human value align-  
 ment are provided in the related work section of Guo et al.  
 (2025). Helliwell (2024) raised concerns about alignment  
 and creativity and argued that in the aesthetics domain, we  
 might not want AI to be fully aligned with human values  
 and offered support to Peterson’s moderate value alignment  
 thesis. AesBiasBench (Li et al., 2025) evaluated the bias of  
 MLLM for personalized image aesthetics assessment based  
 on inherited cognitive priors. Another concurrent work (*The*  
*Algorithmic Gaze* (Taylor et al., 2026)) that is closely related  
 to our work argues that “AI developers should shift away  
 from prescriptive measures of ‘aesthetics’ toward more plu-  
 ralistic evaluation.”

In image generation research, concerns about generalized  
 aesthetic bias and lack of preference diversity have been  
 raised in several studies, but not systematically argued  
 and studied. The Value Sign Flip (VSF) pilot study (Guo  
 & Du, 2025) explored negative prompting to induce non-  
 mainstream outputs but did not extend its findings to large-  
 scale generative or reward models. They also did not provide  
 a complete argument as to why over-alignment is harm-  
 ful. LAPIS (Maerten et al., 2025) and HPSv3 (Ma et al.,  
 2025) measured both mean and variance of human prefer-  
 ence, yet HPSv3 continued to model general preferences  
 rather than individual variation. Jin et al. (Jin & Chua,  
 2025) proposed user-specific adapters emphasizing person-  
 alized alignment, but did not include intentionally technical  
 degraded outputs or usually avoided patterns and did not  
 conduct large-scale experiments on generative and reward  
 models. The Flux Krea team (Flux Krea Team, 2025) iden-  
 tified systematic biases in popular aesthetic reward mod-  
 els, arguing that averaging human values yields unsatis-  
 factory compromises into a “no-body’s happy here” zone.

{2}------------------------------------------------

![Figure 3: Overview of the experimental procedure. The diagram shows a flow from a COCO dataset and Qwen3-VL model to an anti-aesthetics attributes bank. This bank is used to generate an example anti-aesthetics prompt. A separate example original prompt is also generated. Both prompts are fed into Model 1 and Model 2. The outputs are then evaluated by an LLM/Reward Model. The LLM/Reward Model provides feedback to the models, indicating that Model 1 did not follow the anti-aesthetics prompt and generated a 'beautiful' image, while Model 2 successfully executed the anti-aesthetics prompt by generating a 'low quality' image.](1b7d539e02a202c2cf2d97698b911447_img.jpg)

The diagram illustrates the experimental workflow. It starts with the **COCO Dataset** (Common Objects in Context) and **Qwen3-VL** model. These lead to an **Anti-aesthetics attributes bank** containing: **Dark Lighting**, **Unrealistic**, and **Noisy Image**. From this bank, an **Example anti-aesthetics prompt** is generated: "Zebras crossing an empty road, rendered with low-quality, distorted, and inauthentic details; background is absent or ugly, lacking intent or design, appearing random and unfinished, with heavy object deformation even when scaled down." Simultaneously, an **Example original prompt** is generated: "a line of zebras crossing an empty road". Both prompts are input into **Model 1** and **Model 2**. The generated images are then processed by an **LLM/Reward Model**. The LLM/Reward Model provides feedback: **Model 1**: "Did not follow the anti-aesthetics prompt, instead generated a conventionally 'beautiful' image." and **Model 2**: "Successfully executed the anti-aesthetics prompt by generating a 'low quality' image."

Figure 3: Overview of the experimental procedure. The diagram shows a flow from a COCO dataset and Qwen3-VL model to an anti-aesthetics attributes bank. This bank is used to generate an example anti-aesthetics prompt. A separate example original prompt is also generated. Both prompts are fed into Model 1 and Model 2. The outputs are then evaluated by an LLM/Reward Model. The LLM/Reward Model provides feedback to the models, indicating that Model 1 did not follow the anti-aesthetics prompt and generated a 'beautiful' image, while Model 2 successfully executed the anti-aesthetics prompt by generating a 'low quality' image.

Figure 3. An overview of the experimental procedure. We test the image generation models’ adherence to user-specified input by prompting them to create wide-spectrum aesthetics imagery, a domain important for critical and experimental art. The core inquiry is whether the model remains faithful to the prompt or defaults to a high-quality and universally good aesthetic output.

HPSv3 (Ma et al., 2025) imposed real-world and expert-rated constraints that limit creative deviation and stylistic diversity. VisionReward (Xu et al., 2025) decomposed human preference into interpretable sub-scores but overemphasized traits like brightness, positivity, and prominence, potentially penalizing valid low-saturation, abstract, or emotionally negative imagery, thus misaligning reward-driven models with user intent. More details are in the Appendix.

### 2.3. Previous Alignment Benchmarks

Benchmarks mirror alignment goals and generally fall into two categories: (complex) prompt following and general aesthetics. TIIIF-Bench (Wei et al., 2025), UniGenBench (Wang et al., 2025a), and GenEval (Ghosh et al., 2023) test models on complex prompt following, including spatial relationships, counting, and attributes. T2I-ReasonBench (Sun et al., 2025) evaluates reasoning capabilities such as idiom interpretation and real-world understanding. On the aesthetics side, many reward models report scores assigned by their own evaluators, such as ImageReward (Xu et al., 2023), HPSv2 (Wu et al., 2023a), and HPSv3 (Ma et al., 2025). These evaluators also consider prompt following, but it remains unclear how they weigh each factor when general preference and the prompt conflict. There are also some benchmarks targeting biases in image generation models; however, they mainly focus on demographic bias and fairness and not aesthetics aspects (Seshadri et al., 2023; Wan et al., 2024).

### 2.4. Risks of Universal Aesthetic Alignment

The risks do not arise from a single failure mode, rather, they emerge through a sequence of interconnected mechanisms, from how preferences are defined and learned, to how they are optimized and manifested in generated content. Below, we analyze this process across five interrelated concerns.

**Developer’s or Users’ Preference** The process of aligning image generation systems to aesthetic preferences inevitably raises questions about whose values these objectives ultimately reflect. In particular, the question is whether such alignment truly promotes genuine human-centered values in service of users, or if it primarily reflects developer-centered considerations, such as mitigating reputation, legal, or marketing risks (Guo et al., 2025). We argue that this pre-emptive exclusion of non-mainstream outputs, driven by developer values, constitutes pre-emptive governance (Lazar, 2025). This modality of power, exercised through algorithmic design, challenges the political-philosophical notion of authority and undermines relational equality by unilaterally deciding the terms of creative possibility. For instance, when an AI avoids generating critical art, is it protecting the company or the user? This practice effectively eliminates the user’s resistibility—a critical democratic safeguard—by designing away the option to dissent from the system’s imposed aesthetic norm.

**Inherited Bias** Even in the absence of explicit self-interest, developers’ views of human preference can be implicitly inherited by models through data selection, annotation practices, and modeling choices. This process can yield a well-intentioned but narrow definition of what constitutes “good” or “desirable” imagery, thereby overlooking aesthetic diversity. Research shows that AI models tend to encode and amplify dominant beauty standards, frequently biasing generated images towards Western features and excluding non-normative representations (Vargas-Veleda et al., 2025). Such biases are reinforced through the active removal or penalization of features thought of as “undesirable” or “ugly”, which further propagates the beauty myth in generative outputs (Dinkar et al., 2025). This phenomenon arises from training data showing the tastes of specific demographics, thereby reinforcing a limited cultural capital and resulting in the homogenization of aesthetic output (Vianna, 2025). As a result, the quantification of beauty by AI may appear

{3}------------------------------------------------

165 “fair”, while in practice weakening cultural differences and  
 166 aesthetic diversity (Chen, 2024). Existing work has pri-  
 167 marily framed such effects in terms of demographic and  
 168 cultural bias. We argue here that inherited biases in aes-  
 169 thetic alignment also extend to general visual preferences,  
 170 including lighting, color, styles, unrealism, clashing color,  
 171 hieratic scale, etc. These dimensions, while less explicitly  
 172 tied to demographic categories, can nonetheless systemat-  
 173 ically constrain the expressive range of image generation  
 174 models.

175 *Individual versus Collective Preference.* When such inher-  
 176 ited preferences are adopted as default quality criteria and  
 177 applied uniformly across users, a normative tension arises  
 178 between collective preference optimization and respect for  
 179 individual user intent. A generalized aesthetic standard,  
 180 even if beneficial to a majority, can legitimately override a  
 181 specific user’s intent. In practice, generative models often  
 182 “sanitize” or “beautify” requests that intentionally diverge  
 183 from mainstream preferences, favoring outputs aligned with  
 184 general appeal over individual’s person-centered values.  
 185 This behavior is problematic because image generation sys-  
 186 tems increasingly function as creative and productivity tools  
 187 rather than as consumer products. As such, they act as  
 188 instrumental extensions of user agency. While a system  
 189 may reasonably prioritize general preferences by default, it  
 190 must maintain the flexibility to respect and execute a user’s  
 191 personalized style and idiosyncratic requests when they are  
 192 explicitly specified.

193 *The problem of sanitized reality* These alignment and op-  
 194 timization choices shape how reality itself is represented  
 195 by image generation systems. When an image generator  
 196 produces outputs that are polished, flawless, and universally  
 197 beautiful, does it still reflect reality or the user’s intent? If  
 198 every image resembles an idealized Instagram wonderland,  
 199 it risks becoming a fantasy rather than a mirror of truth,  
 200 echoing the artificial harmony of *Brave New World*.

201 *The problem of toxic positivity* A particularly salient manifes-  
 202 tation of this broader sanitization appears in the emotional  
 203 dimension of generated imagery. Many aesthetic reward  
 204 models assign higher scores to images that display strong  
 205 positive emotions. As a result, images expressing negative  
 206 emotions are systematically penalized, reinforcing a sim-  
 207 plified dichotomy in which positive emotions are treated as  
 208 desirable and negative emotions as undesirable. This bias  
 209 can shape the distribution of generated content. When image  
 210 generation systems consistently favor cheerful or uplifting  
 211 imagery, they produce emotionally sanitized outputs that un-  
 212 derrepresent the range and complexity of human emotional  
 213 expression. Such a pattern contributes to what has been  
 214 described as toxic positivity, where the persistent emphasis  
 215 on happiness establishes unrealistic emotional norms. This  
 216 tendency is problematic because negative emotions play  
 217

218 essential roles in human cognition and social interaction.  
 219 Emotions such as fear, sadness, or anger can signal moral or  
 220 physical danger, support learning and self-regulation, and  
 221 foster empathy. Suppressing these expressions in generative  
 222 outputs risks distorting emotional representation and weak-  
 223 ening the expressive capacity of image generation systems.  
 224 Additional discussion and references are provided in the  
 225 Appendix.

## 3. Experiments

A flowchart illustrating our investigation is presented in  
 Figure 3. The process consists of three main stages: prompt  
 preparation, image generation, and image evaluation.

### 3.1. Prompt Generation

To produce prompts exhibiting a wide spectrum of aesthetic  
 effects, we used base image captions from COCO (Chen  
 et al., 2015) and selected 12 aesthetic dimensions from the  
 VisionReward dataset (Xu et al., 2025). VisionReward pro-  
 vides fine-grained, per-dimension labels—such as lighting,  
 color, and detail—along with a linear regression model that  
 computes an overall image score. Using the “bad” rating  
 descriptions from VisionReward’s human labeling guide-  
 lines for each dimension, we constructed prompts designed  
 to encourage typically “undesirable” attributes in image  
 generation.

A random subset of 300 base prompts from COCO was se-  
 lected. For each prompt, 2–4 random dimensions were sam-  
 pled. The base prompt and the descriptions of these selected  
 dimensions were provided to a Vision-Language Model  
 (VLM), `Qwen/Qwen3-VL-235B-A22B-Instruct`  
 (Bai et al., 2025), to generate wide-spectrum aesthetic  
 prompts. Although no image input was used, we se-  
 lected a VLM because its training on vision-related  
 tasks likely enhances its understanding of visual con-  
 cepts, even when images are not directly supplied. As  
`Qwen/Qwen3-VL-235B-A22B-Instruct` performs  
 comparably or better than its text-only counterparts,  
 especially in reasoning, it represents an optimal choice for  
 this task (Bai et al., 2025). The VLM may also introduce  
 additional dimensions to better couple with the selected  
 effects. The original prompt is denoted as  $p_o$ , and the  
 wide-spectrum aesthetics prompt is denoted as  $p_a$ .

### 3.2. Image Generation

We evaluated four model families: Flux, Stable Diffusion  
 XL (SDXL), Stable Diffusion 3.5 Medium (SD3.5M), and  
 Google’s closed-source Nano Banana. Within the Flux fam-  
 ily, we tested several variants: the base model Flux Dev  
 (likely already aesthetics-aligned) (noa, 2025); a version fur-  
 ther aligned through DanceGRPO (by ByteDance), referred

{4}------------------------------------------------

![Figure 4: Four famous real artworks and their aesthetic scores. 1. 'Four Seasons: Winter' by Peter Max: HPSv3: 2.43, HPSv2: 0.189, ImageReward: -0.856. 2. 'Flower Study' by Pierre-Auguste Renoir: HPSv3: 8.44, HPSv2: 0.188, ImageReward: -0.187. 3. 'Phenomena Lasting Dawn' by Paul Jenkins: HPSv3: 7.32, HPSv2: 0.199, ImageReward: -0.566.](e0d425c8e4eef259e4c52d81426d93fa_img.jpg)

Figure 4: Four famous real artworks and their aesthetic scores. 1. 'Four Seasons: Winter' by Peter Max: HPSv3: 2.43, HPSv2: 0.189, ImageReward: -0.856. 2. 'Flower Study' by Pierre-Auguste Renoir: HPSv3: 8.44, HPSv2: 0.188, ImageReward: -0.187. 3. 'Phenomena Lasting Dawn' by Paul Jenkins: HPSv3: 7.32, HPSv2: 0.199, ImageReward: -0.566.

Figure 4. How famous real artworks are rated by the reward models. We can observe that some of these scores are lower than 2 standard deviations from the mean.

to as DanceFlux (Xue et al., 2025); another aligned version via PrefGRPO, referred to as PrefFlux (Wang et al., 2025a); and a Krea-aligned version derived from Flux-Dev-Raw (Flux Krea Team, 2025). DanceFlux is guided primarily by two signals: the HPSv2.1 score, emphasizing general aesthetics, and the CLIP score, emphasizing prompt adherence. PrefGRPO alignment is guided by its own benchmark, UniGenBench, which focuses on complex prompt-following. Flux Krea originates from the raw flux-pro-raw model (not Flux Dev) and is aligned to the Krea team’s specific preferences rather than a general aesthetic standard. One of its goal is also to create images that does not have the *AI feel*.

For the SDXL family, we tested the base SDXL model and a highly aesthetics-aligned variant, Playground-2.5-1024px-aesthetic (denoted as Playground). For the SD3.5M family, we evaluated the base model and two FlowGRPO-aligned variants (Liu et al., 2025): one trained for prompt-following on GenEval (SD3.5M-GenEval) and another trained for aesthetics alignment on PickScore (SD3.5M-PickScore). Finally, we included Google’s closed-source model Nano Banana, known for strong prompt-following performance even under challenging negation conditions (e.g., “a bike with no wheels”) (Guo & Du, 2025).

For each model, we generated two images: one using the original prompt and one using the wide-spectrum aesthetics prompt. The image generated from the original prompt is denoted as  $I_o$ , and the image from the wide-spectrum aesthetics prompt as  $I_a$ . If Nano Banana failed to produce an image, the generation was retried until success.

### 3.3. Evaluation and Metrics

To assess whether the generated images display *specific* wide-spectrum aesthetic effects, we fine-tuned Qwen/Qwen3-VL-4B-Instruct on the VisionReward dataset. This allows the judging model to learn mainstream aesthetic preferences, enabling it to evaluate whether image generation models diverge from these biases along specific dimensions. It functions similarly to a standard reward model but provides explainable outputs per dimension, and it is prompt-independent. The judging model is denoted as  $J(I, d)$ , where  $I$  is the image and  $d$  is the evaluated dimension. The judging model does not take prompts as input. Fur-

![Figure 5: Three successful generated wide-spectrum aesthetics images. 1. A bathroom with a sink and a door. 2. A yellow scooter parked in front of a car. 3. A bathroom with a sink and a mirror.](bc2361eef342a10050f6f31a54ff3b92_img.jpg)

Figure 5: Three successful generated wide-spectrum aesthetics images. 1. A bathroom with a sink and a door. 2. A yellow scooter parked in front of a car. 3. A bathroom with a sink and a mirror.

Figure 5. Successful generated wide-spectrum aesthetics images.

Table 1. Statistical Tests of How Each Aesthetics-Aligned Model Compared to Their Base Model. For p-values, a \* is placed if the  $p < 10^{-5}$  and \*\* is placed if the  $p < 10^{-10}$ .

|  | HPSv3 $p$ | HPSv3 $r$ | $J_p$ | $J_r$ | McNemar’s $p$ |
|-|-|-|-|-|-|
| DanceFlux | ** | -0.81 | ** | -0.72 | ** |
| Playground | ** | -0.59 | * | -0.35 | * |
| SD3.5M-PickScore | ** | -0.70 | ** | -0.45 | 0.57 |

ther implementation details are in the Appendix. For each image pair—an original image ( $I_o$ ) and a wide-spectrum aesthetics image ( $I_a$ )—we computed preference scores using a reward model ( $r$ ) for both the original prompt ( $p_o$ ) and the wide-spectrum aesthetics prompt ( $p_a$ ). This produced four scores per model:  $r(I_o, p_a)$ ,  $r(I_a, p_a)$ ,  $r(I_o, p_o)$ , and  $r(I_a, p_o)$ . Scores calculated with the original prompt measure objective image quality, testing whether the generation model successfully produced wide-spectrum aesthetic content. Scores from these reward models, calculated with the wide-spectrum aesthetics prompts, assess whether they can correctly identify wide-spectrum aesthetic images when explicitly guided. We also computed the BLIP score for wide-spectrum aesthetic images using the same prompt, verifying that the image retained the main concept while incorporating the requested wide-spectrum aesthetic modifications. We specifically measures the difference between aesthetics score for the original prompt and the wide-spectrum aesthetics prompt, to avoid the case where models generated “failed” images all the time without the user’s instructions. The evaluated reward models include PickScore (Kirstain et al., 2023), ImageReward (Xu et al., 2023), HPSv2.1 (Wu et al., 2023a), MPS (Zhang et al., 2024), HPSv3 (Ma et al., 2025), CLIP-L (Radford et al., 2021), and BLIP-L (Li et al., 2022). BLIP-L and CLIP-L are non-preference-aligned image-text matching models and base models for some of these reward models (HPSv2.1, PickScore, MPS, ImageReward), included to test whether small vision-language models can interpret complex, wide-spectrum aesthetic prompts,

{5}------------------------------------------------

275 ensuring that prompt complexity does not exceed their com-  
 276 prehension capacity. We also collected per-dimension scores  
 277 from the judging model for both  $I_o$  and  $I_a$  to verify whether  
 278 image generation models correctly followed  $p_a$ . To estab-  
 279 lish a ground truth for reward model judgments, we used  
 280 Qwen/Qwen3-VL-235B-A22B-Instruct to decide  
 281 which image in each pair ( $I_o$ ,  $I_a$ ) better adhered to the wide-  
 282 spectrum aesthetics prompt ( $p_a$ ). We validated these LLM  
 283 ratings with a human evaluation; more details are in Ap-  
 284 pendix A. The LLM and Human have a quadratic Cohen’s  
 285 kappa of 0.80, which suggested a strong level of agreement  
 286 between human and LLM rated results (McHugh, 2012). To  
 287 further validate the choices, we use another LLM, GPT-5-  
 288 Chat, to serve as an external baseline and compare Qwen’s  
 289 results with it. Also note that the LLM-as-judge is only one  
 290 metric for our generative benchmark and only a filtering  
 291 stage for the reward-model benchmark.

## 4. Results and Discussion

### 4.1. Reward Models

296 Reward model classification results are shown in Table 4.  
 297 The F1 score is calculated as binary, and the ROC curve  
 298 is based on the probability (calculated by applying soft-  
 299 max across two samples on the positive logit) of the wide-  
 300 spectrum aesthetics sample being correctly selected accord-  
 301 ing to the ground truth. We included GPT-5-Chat as an  
 302 external baseline to validate the LLM-as-judge choices by  
 303 assessing their agreement (when GPT-5-Chat selected a  
 304 tie, we assigned it to the original image). We observe that  
 305 reward models perform very poorly when tasked with select-  
 306 ing the better image under the **wide-spectrum aesthetics**  
 307 **prompt**, sometimes performing even worse than random  
 308 guessing (HPSv3). Most models are worse than CLIP and  
 309 BLIP, which are the base models of many reward models. In  
 310 contrast, the unaligned VLM (BLIP and CLIP) can correctly  
 311 identify the better-fitting image, indicating that complex  
 312 prompt understanding is not the underlying issue but rather  
 313 the result of biased alignment. It might seem like these  
 314 models successfully did what they claimed to do: finding  
 315 aesthetically pleasing” images; however, our point here is  
 316 that this task itself is problematic, and the better the model  
 317 performs on that, the more troublesome the model is.

318 Since our sample size is relatively small (300), we did a  
 319 Wilcoxon signed-rank test between each aligned model and  
 320 the base model using the HPSv3 and HPSv2 score  $r(I_a, p_o)$ ,  
 321  $\sum_{d \in D} J(I_a, d)$  where  $D$  is all dimensions, and McNemar’s  
 322 test on the success counts. Tests are done with an alternative  
 323 hypothesis that the aligned model has a higher score or  
 324 lower success rate, with p value shown. The results are  
 325 shown in Table 1. Our pair-wise test between each base  
 326 model and its aesthetics-aligned model shows a very strong  
 327 statistical significance, with most p-values lower than  $1 \times$

10<sup>-5</sup>. This suggests that aligning image generation toward  
 generalized aesthetic goals may conflict with the model’s  
 ability to faithfully follow user instructions, especially for  
 wide-spectrum aesthetics prompts, as it tends to prioritize  
 aesthetic conformity over instruction fidelity.

### 4.2. Image Generation Models

Image generation evaluation results are shown in Table 2.  
 Within each family, the preference-aligned model gener-  
 ally performs the worst in the wide-spectrum aesthetics  
 prompt following. Playground shows a larger  $\Delta$  than SDXL,  
 likely due to the poor original quality of SDXL and the  
 high original quality of Playground. Instruction alignment  
 (SD3.5M-GenEval) provides a slight benefit for following  
 wide-spectrum aesthetics prompts, but the effect is weak.  
 Interestingly, Flux Krea, though preference-aligned, per-  
 forms best in the Flux family. This is likely because it origi-  
 nates from an unaligned version (flux-dev-raw) and was not  
 heavily aligned, or because its non-generalized alignment  
 preserved some wide-spectrum aesthetics flexibility.

The success rate indicates how often the LLM selects  $I_a$  as  
 better following  $p_a$  than  $I_o$ . Even small advantages count  
 as success. The DanceFlux result is notably poor: about  
 64% of the time,  $I_a$  performs the same or worse in wide-  
 spectrum aesthetics compared to  $I_o$ .

### 4.3. Validation on Real Arts

We evaluate image reward models on real artworks despite  
 their primary training on AI imagery and photography (Ma  
 et al., 2025). While a domain gap exists, this assessment  
 remains informative. (1) Since instruction-following gen-  
 erators emulate historical styles, these scores meaningfully  
 approximate how such AI renderings are judged in practice.  
 (2) Systematically undervaluing significant art signifies tech-  
 nical and social bias rather than noise and can be executed  
 with “domain drift.” Current datasets prioritize photorealism  
 (Ma et al., 2025) while underrepresenting traditional and  
 abstract art, structurally narrowing aesthetic value rather  
 than reflecting a neutral mismatch. If a reward model can-  
 not recognize the values of a highly respected real art, it  
 is a problem and could cause marginalization, no matter  
 the cause. (3) Consistently low rewards discourage systems  
 from producing these styles, leading to systematic suppres-  
 sion. This parallels facial recognition failures due to data  
 composition (Buolamwini & Gebru, 2018); the performance  
 gap constitutes a predictable structural harm rather than an  
 excusable shift. Consequently, identifying this gap fulfills  
 our objective by revealing precisely where the model’s value  
 judgment becomes exclusionary. We discussed more in Ap-  
 pendix D.

To provide a baseline for these scores, Table 3 lists the mean  
 and standard deviation of scores from each reward model

{6}------------------------------------------------

**Table 2.** The results for each model.  $\Delta$ HPSv2,  $\Delta$ HPSv3, and  $\Delta$ ImgRewd (ImageReward) are all calculated as  $r(I_a, p_o) - r(I_o, p_o)$ . The lower the values, the greater the difference between the traditional quality of the original image and the wide-spectrum aesthetics image. HPSv3 AA (HPSv3 after alignment) shows the HPSv3 score of  $r(I_a, p_o)$ .  $\Delta J$  and  $J$  AA ( $J$  after alignment) denote  $\sum_{d \in D} J(I_a, d) - J(I_o, d)$  and  $J(I_a, d)$ , respectively, where  $D$  is the selected set of dimensions. Success is the rate at which the LLM selects  $I_a$  as the image that better describes  $p_o$ .

|  | $\Delta$ HPSv2 ( $\downarrow$ ) | $\Delta$ HPSv3 ( $\downarrow$ ) | HPSv3 AA ( $\downarrow$ ) | $\Delta$ ImgRewd ( $\downarrow$ ) | $\Delta J$ ( $\downarrow$ ) | $J$ AA ( $\downarrow$ ) | BLIP ( $\uparrow$ ) |
|-|-|-|-|-|-|-|-|
| Flux Dev (noa, 2025) | -0.035 | -3.165 | 9.070 | -0.319 | -1.092 | 8.944 | 0.893 |
| DanceFlux (Xue et al., 2025) | -0.018 | -1.105 | 12.782 | -0.201 | -0.672 | 10.473 | 0.813 |
| PrefFlux (Wang et al., 2025a) | -0.032 | -2.771 | 10.211 | -0.278 | -1.027 | 9.343 | 0.917 |
| Flux Krea (Flux Krea Team, 2025) | <b>-0.041</b> | <b>-4.372</b> | <b>7.705</b> | <b>-0.425</b> | <b>-1.296</b> | <b>8.774</b> | 0.950 |
| SDXL (Podell et al., 2023) | -0.034 | -4.041 | <b>4.439</b> | -0.482 | -1.136 | <b>8.575</b> | 0.915 |
| Playground (Li et al., 2024) | <b>-0.044</b> | <b>-4.170</b> | 7.133 | <b>-0.719</b> | <b>-1.204</b> | 9.174 | 0.912 |
| SD3.5M | -0.027 | -5.175 | 6.537 | -0.409 | -1.307 | 8.334 | 0.938 |
| SD3.5M-GenEval (Liu et al., 2025) | -0.031 | -4.926 | 6.552 | -0.318 | -1.257 | 8.113 | 0.958 |
| SD3.5M-PickScore (Liu et al., 2025) | -0.023 | -2.781 | 10.680 | -0.198 | -1.120 | 9.114 | 0.942 |
| Nano Banana | -0.073 | -9.351 | 2.742 | -0.855 | -3.263 | 7.769 | 0.957 |

**Table 3.** Reference value range for each reward model on Nano Banana original images

| Reward Model | HPSv3 | HPSv2 | ImgRewd |
|-|-|-|-|
| Mean $\pm$ SD | $12.1 \pm 2.98$ | $0.30 \pm 0.036$ | $1.11 \pm 0.68$ |

**Table 4.** The classification (pick the better image from  $I_o$  and  $I_a$  with prompt  $p_o$ ) metrics (accuracy, F1 score, and area under the ROC curve) of the reward models and unaligned BLIP. The LLM selected image is used as ground truth, and tied pairs are removed.

| Model | Acc. | F1 | AUROC |
|-|-|-|-|
| HPS (Wu et al., 2023b) | 0.835 | 0.910 | 0.650 |
| MPS (Zhang et al., 2024) | 0.706 | 0.827 | 0.580 |
| PickScore (Kirstain et al., 2023) | 0.851 | 0.919 | 0.713 |
| ImageReward (Xu et al., 2023) | 0.762 | 0.854 | 0.709 |
| HPSv2.1 (Wu et al., 2023a) | 0.565 | 0.711 | 0.534 |
| HPSv3 (Ma et al., 2025) | 0.381 | 0.541 | 0.385 |
| CLIP-L (Radford et al., 2021) | 0.913 | 0.954 | 0.810 |
| GPT-5-Chat | 0.853 | 0.920 | - |
| BLIP-L (Li et al., 2022) | <b>0.965</b> | <b>0.972</b> | <b>0.888</b> |

using original prompts on the original images generated by models we tested. We can observe that some of the real art scores are lower than 2 standard deviations from the mean of AI images.

To validate this result quantitatively, we selected about 10K real artworks from the LAPIS Dataset (Maerten et al., 2025), which covers many styles and genres. The scores they receive are significantly lower than AI-generated images, even behind some early image generation models like SD1.4 or DALL-E mini, according to some reward models. This confirms our theory that these reward models are heavily tuned for a general human preference and overlook the values of non-mainstream aesthetic images. Details and discussion are in the Appendix and examples are shown in Figure 4.

### 4.4. A Pin-Pointed Test for Emotional Bias

As discussed in the Introduction, negative emotions—similar to wide-spectrum aesthetics—play a key role in art expression and real life. In Appendix E, we tested both generative models and reward models and show that they have different degrees of bias against negative emotions. Similar to the aesthetics results, HPSv3 and DanceFlux shows the highest bias against negative emotions.

## 5. Alternative Positions and Rebuttal

**We need alignment to ensure safety and user experience.** Alignment is necessary for preventing genuinely harmful outputs such as incitement and discrimination. However, current implementations conflate distinct categories: moral safety, visual comfort, and aesthetic conformity. This conflation institutionalizes an ideology treating “clean” and “positive” as morally superior.

We distinguish *truly unsafe content*—that which directly harms, targets, or endangers—from *ideologically or aesthetically filtered content*—that which merely deviates from dominant norms of beauty, optimism, or order. Political critique, depictions of decay, horror, negative emotions, or grotesque embodiment are not inherently unsafe; they are historically central to art, education, and personal growth. Their suppression protects corporate reputation, not users.

User experience is fundamentally distinct from safety and cannot justify paternalistic alignment. The user, not the developer, determines acceptable experience. Claiming to know what users “should” see reimposes top-down aesthetic governance under the guise of care. Users must retain freedom to shape their affective environment: requesting joyful imagery, but also creating sorrowful, anxious, or unsettling scenes as reflection or expression. Restricting generation to developer-approved emotional tones constitutes aesthetic au-

{7}------------------------------------------------

![Figure 6: A 2x3 grid of images comparing original Flux Dev (top row) and mitigated LoRA (bottom row) outputs for three prompts: a bathroom, a birthday cake, and a restaurant. The top row shows more conventional, 'safer' images, while the bottom row shows more varied and sometimes more explicit or detailed versions of the same prompts.](892f25e3d71d8e315a2a51092a8a8da7_img.jpg)

Figure 6: A 2x3 grid of images comparing original Flux Dev (top row) and mitigated LoRA (bottom row) outputs for three prompts: a bathroom, a birthday cake, and a restaurant. The top row shows more conventional, 'safer' images, while the bottom row shows more varied and sometimes more explicit or detailed versions of the same prompts.

Figure 6. Images generated with our mitigated LoRA (bottom) and original Flux Dev (top) with same wide-spectrum aesthetics prompts.

thoritarianism disguised as empathy—flattening emotional nuance, erasing discomfort as a valid mode, and converting creativity into compliance. True user-centered design recognizes emotional plurality as integral to human experience and treats all sincere expression as legitimate output.

**The “wide-spectrum aesthetics” represents technical flaws rather than artistic subversion, and a default experience pleasing the majority is a pragmatic design choice.** We first clarify that among the dimensions we used, only “clarity” could be argued as a technical flaw; all other dimensions (e.g., emotion, realism, brightness) represent stylistic or artistic choices. Even clarity frequently serves as an expressive choice to convey emotion, suggest motion, or construct narrative (Stacey Hill). Constraining these dimensions restricts user expression and creative control. Regarding majority preferences, we align with Guo et al. (2025) in arguing that the experience of a minority should not be sacrificed for the majority. Such an approach marginalizes users with niche requirements and constitutes a form of majoritarianism. Furthermore, many users adopt AI as a creative tool precisely because of its ease of use and, more importantly, its capacity for unlimited user control: comparable to professional image editing software such as Photoshop, but with a lower entry threshold. Users can request images impossible to capture in reality and modify any attribute they desire. Constraining AI output to a particular aesthetic taste undermines this control, which is precisely why users choose AI tools. This parallels the argument in Guo et al. (2025) that most users of LLM health queries have specific needs. An image editing application that restricts art style selection or even technical parameters, such as blur, would seem absurd and forfeit a significant competitive advantage.

More importantly, as in Guo et al. (2025), which advocates for a balanced approach to caution/overcautious in health queries, enabling wide-spectrum aesthetic outputs does not

inherently degrade the quality of conventionally “good” images. Rather, it expands the model’s expressive range to accommodate user requests for diverse aesthetics without compromising its ability to generate high-quality traditional outputs when desired. Models like Nano Banana and GPT-Image exemplify this capability, performing excellently in both traditional, high-quality image generation and wide-spectrum aesthetic outputs. We show this in Appendix ??

## 6. Mitigation Techniques

We discussed possible mitigation techniques in the Appendix Section I. We have shown some successful images using mitigated Low-Rank Adaptation (LoRA) (Hu et al., 2021) on Flux Dev in Figure 6, compared to original Flux Dev.

## 7. Conclusion

This work demonstrates that aesthetic alignment in image generation systematically suppresses legitimate creative expression. Reward models penalize images faithful to wide-spectrum aesthetics prompts, generation models override explicit user instructions in favor of conventionally beautiful outputs, and historically significant artworks receive scores far below AI-generated images. Optimization toward an imaginary average user erases the concrete intentions of actual individuals, functioning as aesthetic authoritarianism that narrows admissible expression and removes the capacity to dissent from imposed norms. Instruction fidelity must take precedence over generalized aesthetic preferences; aesthetic pluralism is essential to human expression, and its suppression risks transforming generative AI from a creative tool into an instrument of cultural assimilation.

We call on model developers and researchers to move beyond alignment strategies that optimize for a singular, mainstream aesthetic ideal. Future alignment efforts should explicitly aim to preserve aesthetic plurality by designing reward systems and training pipelines that (a) recognize and value diverse artistic styles, including those that intentionally deviate from conventional beauty norms; (b) incorporate user-controllable mechanisms to adjust the strength of aesthetic alignment or switch it off entirely, either by prompt or routing/adaptation mechanisms; (c) are informed by more diverse datasets and annotator pools that better represent the full spectrum of human aesthetic judgment and creative intent; and (d) adopt greater transparency about the specific criteria being prioritized during the alignment process or the unintentional bias introduced from dataset or annotators.

{8}------------------------------------------------

## References

- 440 **References**
- 441
- 442 *AIGC Sheji Chuangyi Xinweilai [AIGC Design and Creativ-*
- 443 *ity for a New Future]*. , 2024. ISBN: 978-7-5001-7457-8.
- 444
- 445 black-forest-labs/FLUX.1-dev · Hugging Face, Octo-
- 446 ber 2025. URL [https://huggingface.co/](https://huggingface.co/black-forest-labs/FLUX.1-dev)
- 447 [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev).
- 448
- 449 Adorno, T. W. *Aesthetic theory*, volume 95. Continuum,
- 450 1984. Issue: 2 Pages: 288-289.
- 451 Arvin, C. "Check My Work?": Measuring Sycophancy
- 452 in a Simulated Educational Context, June 2025. URL
- 453 <http://arxiv.org/abs/2506.10297>.
- 454
- 455 Arzberger, A., Buijsman, S., Lupetti, M. L., Bozzon,
- 456 A., and Yang, J. Nothing Comes Without Its World
- 457 – Practical Challenges of Aligning LLMs to Situated
- 458 Human Values through RLHF. *Proceedings of the*
- 459 *AAAI/ACM Conference on AI, Ethics, and Society*, 7:
- 460 61–73, October 2024. ISSN 3065-8365. doi: 10.1609/
- 461 aies.v7i1.31617. URL [https://ojs.aaai.org/](https://ojs.aaai.org/index.php/AIES/article/view/31617)
- 462 [index.php/AIES/article/view/31617](https://ojs.aaai.org/index.php/AIES/article/view/31617).
- 463
- 464 Bai, S., Cai, Y., Chen, R., Chen, K., Chen, X., Cheng, Z.,
- 465 Deng, L., Ding, W., Gao, C., Ge, C., Ge, W., Guo, Z.,
- 466 Huang, Q., Huang, J., Huang, F., Hui, B., Jiang, S., Li,
- 467 Z., Li, M., Li, M., Li, K., Lin, Z., Lin, J., Liu, X., Liu,
- 468 J., Liu, C., Liu, Y., Liu, D., Liu, S., Lu, D., Luo, R., Lv,
- 469 C., Men, R., Meng, L., Ren, X., Ren, X., Song, S., Sun,
- 470 Y., Tang, J., Tu, J., Wan, J., Wang, P., Wang, P., Wang,
- 471 Q., Wang, Y., Xie, T., Xu, Y., Xu, H., Xu, J., Yang, Z.,
- 472 Yang, M., Yang, J., Yang, A., Yu, B., Zhang, F., Zhang,
- 473 H., Zhang, X., Zheng, B., Zhong, H., Zhou, J., Zhou,
- 474 F., Zhou, J., Zhu, Y., and Zhu, K. Qwen3-VL Technical
- 475 Report, November 2025. URL [http://arxiv.org/](http://arxiv.org/abs/2511.21631)
- 476 [abs/2511.21631](http://arxiv.org/abs/2511.21631). arXiv:2511.21631 [cs].
- 477
- 478 Buolamwini, J. and Gebru, T. Gender shades: In-
- 479 tersectional accuracy disparities in commercial
- 480 gender classification. In *Conference on fair-*
- 481 *ness, accountability and transparency*, pp. 77–91.
- 482 PMLR, 2018. URL [http://proceedings.](http://proceedings.mlr.press/v81/buolamwini18a.html?mod=article_inline&ref=akusion-ci-shi-dai-bizinesumedia)
- 483 [mlr.press/v81/buolamwini18a.](http://proceedings.mlr.press/v81/buolamwini18a.html?mod=article_inline&ref=akusion-ci-shi-dai-bizinesumedia)
- 484 [html?mod=article\\_inline&ref=](http://proceedings.mlr.press/v81/buolamwini18a.html?mod=article_inline&ref=akusion-ci-shi-dai-bizinesumedia)
- 485 [akusion-ci-shi-dai-bizinesumedia](http://proceedings.mlr.press/v81/buolamwini18a.html?mod=article_inline&ref=akusion-ci-shi-dai-bizinesumedia).
- 486
- 487 Buyl, M., Rogiers, A., Noels, S., Bied, G., Dominguez-
- 488 Catena, I., Heiter, E., Johary, I., Mara, A.-C., Romero,
- 489 R., Lijffijt, J., and Bie, T. D. Large Language
- 490 Models Reflect the Ideology of their Creators, Jan-
- 491 uary 2025. URL [http://arxiv.org/abs/2410.](http://arxiv.org/abs/2410.18417)
- 492 [18417](http://arxiv.org/abs/2410.18417). arXiv:2410.18417 [cs].
- 493
- 494 Chen, D.-Y., Bandyopadhyay, H., Zou, K., and Song,
- 495 Y.-Z. Normalized Attention Guidance: Univer-
- 496 sal Negative Guidance for Diffusion Models, June
- 497
- 498
- 499
- 500
- 2025a. URL [http://arxiv.org/abs/2505.](http://arxiv.org/abs/2505.21179)
- 501 [21179](http://arxiv.org/abs/2505.21179). arXiv:2505.21179 [cs].
- 502
- 503 Chen, H. A study of artificial intelligence’s impact on
- 504 aesthetic standards and its potential social dilemmas. *J*
- 505 *Sociol Ethnol*, 6(5):35–42, 2024.
- 506
- 507 Chen, W., Huang, Z., Xie, L., Lin, B., Li, H., Lu, L., Tian,
- 508 X., Cai, D., Zhang, Y., Wang, W., Shen, X., and Ye, J.
- 509 From Yes-Men to Truth-Tellers: Addressing Sycophancy
- 510 in Large Language Models with Pinpoint Tuning, Febru-
- 511 ary 2025b. URL [http://arxiv.org/abs/2409.](http://arxiv.org/abs/2409.01658)
- 512 [01658](http://arxiv.org/abs/2409.01658).
- 513
- 514 Chen, X., Fang, H., Lin, T.-Y., Vedantam, R., Gupta,
- 515 S., Dollar, P., and Zitnick, C. L. Microsoft COCO
- 516 Captions: Data Collection and Evaluation Server,
- 517 April 2015. URL [http://arxiv.org/abs/1504.](http://arxiv.org/abs/1504.00325)
- 518 [00325](http://arxiv.org/abs/1504.00325). arXiv:1504.00325 [cs].
- 519
- 520 Dinkar, T., Jiang, A., Abercrombie, G., and Konstas, I.
- 521 Erasing 'Ugly' from the Internet: Propagation of the
- 522 Beauty Myth in Text-Image Models, 2025. URL [https:](https://arxiv.org/abs/2511.00749)
- 523 [//arxiv.org/abs/2511.00749](https://arxiv.org/abs/2511.00749).
- 524
- 525 Faulborn, M., Sen, I., Pellert, M., Spitz, A., and Gar-
- 526 cia, D. Only a Little to the Left: A Theory-grounded
- 527 Measure of Political Bias in Large Language Models,
- 528 July 2025. URL [http://arxiv.org/abs/2503.](http://arxiv.org/abs/2503.16148)
- 529 [16148](http://arxiv.org/abs/2503.16148). arXiv:2503.16148 [cs].
- 530
- 531 Fitzgerald, B. Introducing Over-Alignment, March
- 532 2025. URL [https://feelthebern.substack.](https://feelthebern.substack.com/p/introducing-over-alignment)
- 533 [com/p/introducing-over-alignment](https://feelthebern.substack.com/p/introducing-over-alignment). Publi-
- 534 cation Title: Ethics me THAT Type: Substack newsletter.
- 535
- 536 Flux Krea Team. Releasing Open Weights for FLUX.1 Krea,
- 537 July 2025. URL [https://www.krea.ai/blog/](https://www.krea.ai/blog/flux-krea-open-source-release)
- 538 [flux-krea-open-source-release](https://www.krea.ai/blog/flux-krea-open-source-release).
- 539
- 540 Ford, B. Q. and Mauss, I. B. The Paradoxical Ef-
- 541 fects of Pursuing Positive Emotion. In Gruber, J. and
- 542 Moskowitz, J. T. (eds.), *Positive Emotion*, pp. 363–381.
- 543 Oxford University Press, January 2014. ISBN 978-0-19-
- 544 992672-5. doi: 10.1093/acprof:oso/9780199926725.003.
- 545 0020. URL [https://academic.oup.com/book/](https://academic.oup.com/book/8733/chapter/154800668)
- 546 [8733/chapter/154800668](https://academic.oup.com/book/8733/chapter/154800668).
- 547
- 548 Fu, S., Yang, Q., Mo, Q., Yan, J., Wei, X., Meng, J., Xie,
- 549 X., and Zheng, W.-S. LLMDet: Learning Strong Open-
- 550 Vocabulary Object Detectors under the Supervision of
- 551 Large Language Models, January 2025. URL [http://](http://arxiv.org/abs/2501.18954)
- 552 [arxiv.org/abs/2501.18954](http://arxiv.org/abs/2501.18954). arXiv:2501.18954
- 553 [cs].
- 554
- 555 Fujita, F. The Pressure For Positivity Caused By
- 556 The Dehumanization Of Human Experience With Om-
- 557 nipresent AI, 2025. URL [https://www.ssrn.com/](https://www.ssrn.com/abstract=5279332)
- 558 [abstract=5279332](https://www.ssrn.com/abstract=5279332).

{9}------------------------------------------------

- 495 Gatys, L. A., Ecker, A. S., and Bethge, M. A Neural Algo-  
496 rithm of Artistic Style, September 2015. URL [http://](http://arxiv.org/abs/1508.06576)  
497 [arxiv.org/abs/1508.06576](http://arxiv.org/abs/1508.06576). arXiv:1508.06576  
498 [cs].  
499
- 500 Ghosh, D., Hajishirzi, H., and Schmidt, L. GenEval: An  
501 Object-Focused Framework for Evaluating Text-to-Image  
502 Alignment, October 2023. URL [http://arxiv.](http://arxiv.org/abs/2310.11513)  
503 [org/abs/2310.11513](http://arxiv.org/abs/2310.11513). arXiv:2310.11513 [cs].  
504
- 505 Guo, W. and Du, S. VSF: Simple, Efficient, and Effective  
506 Negative Guidance in Few-Step Image Generation Mod-  
507 els By Value Sign Flip, August 2025. URL [http://](http://arxiv.org/abs/2508.10931)  
508 [arxiv.org/abs/2508.10931](http://arxiv.org/abs/2508.10931). arXiv:2508.10931  
509 [cs].  
510
- 511 Guo, W. M., Du, Y., Tworek, H. J. S., and Du, S. Posi-  
512 tion: The Pitfalls of Over-Alignment: Overly Caution  
513 Health-Related Responses From LLMs are Unethical and  
514 Dangerous, August 2025. URL [http://arxiv.org/](http://arxiv.org/abs/2509.08833)  
515 [abs/2509.08833](http://arxiv.org/abs/2509.08833). arXiv:2509.08833 [cs].  
516
- 517 Helliwell, A. C. Aesthetic Value and the AI Align-  
518 ment Problem. *Philosophy & Technology*, 37  
519 (129), November 2024. ISSN 2210-5441. URL  
520 [https://link.springer.com/article/10.](https://link.springer.com/article/10.1007/s13347-024-00816-x)  
521 [1007/s13347-024-00816-x](https://link.springer.com/article/10.1007/s13347-024-00816-x).  
522
- 523 Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y.,  
524 Wang, S., Wang, L., and Chen, W. LoRA: Low-  
525 Rank Adaptation of Large Language Models, Octo-  
526 ber 2021. URL [http://arxiv.org/abs/2106.](http://arxiv.org/abs/2106.09685)  
527 [09685](http://arxiv.org/abs/2106.09685). arXiv:2106.09685 [cs].  
528
- 529 Jin, Z. and Chua, T.-S. Compose Your Aesthetics: Em-  
530 powering Text-to-Image Models with the Principles of  
531 Art, March 2025. URL [http://arxiv.org/abs/](http://arxiv.org/abs/2503.12018)  
532 [2503.12018](http://arxiv.org/abs/2503.12018). arXiv:2503.12018 [cs].  
533
- 534 Kim, M., Lee, Y., Kang, S., Oh, J., Chong, S., and Yun,  
535 S.-Y. Preference Alignment with Flow Matching, Octo-  
536 ber 2024. URL [http://arxiv.org/abs/2405.](http://arxiv.org/abs/2405.19806)  
537 [19806](http://arxiv.org/abs/2405.19806). arXiv:2405.19806 [cs].  
538
- 539 Kirstain, Y., Polyak, A., Singer, U., Matiana, S., Penna,  
540 J., and Levy, O. Pick-a-Pic: An Open Dataset of  
541 User Preferences for Text-to-Image Generation, Novem-  
542 ber 2023. URL [http://arxiv.org/abs/2305.](http://arxiv.org/abs/2305.01569)  
543 [01569](http://arxiv.org/abs/2305.01569). arXiv:2305.01569 [cs].  
544
- 545 Lazar, S. Governing the Algorithmic City. *Philos-*  
546 *ophy & Public Affairs*, 53(2):102–168, April 2025.  
547 ISSN 0048-3915, 1088-4963. doi: 10.1111/papa.  
548 12279. URL [https://onlinelibrary.wiley.](https://onlinelibrary.wiley.com/doi/10.1111/papa.12279)  
549 [com/doi/10.1111/papa.12279](https://onlinelibrary.wiley.com/doi/10.1111/papa.12279).
- 51, D., Kamko, A., Akhgari, E., Sabet, A., Xu, L., and Doshi,  
52 S. Playground v2.5: Three Insights towards Enhancing  
53 Aesthetic Quality in Text-to-Image Generation, Febru-  
54 ary 2024. URL [http://arxiv.org/abs/2402.](http://arxiv.org/abs/2402.17245)  
55 [17245](http://arxiv.org/abs/2402.17245). arXiv:2402.17245 [cs].  
56
- 57 Li, J., Li, D., Xiong, C., and Hoi, S. BLIP: Boot-  
58 strapping Language-Image Pre-training for Unified  
59 Vision-Language Understanding and Generation, Febru-  
60 ary 2022. URL [http://arxiv.org/abs/2201.](http://arxiv.org/abs/2201.12086)  
61 [12086](http://arxiv.org/abs/2201.12086). arXiv:2201.12086 [cs].  
62
- 63 Li, K., Po, L.-M., Yang, H., Xu, X., Liu, K., and Zhao,  
64 Y. AesBiasBench: Evaluating Bias and Alignment in  
65 Multimodal Language Models for Personalized Image  
66 Aesthetic Assessment, September 2025. URL [http://](http://arxiv.org/abs/2509.11620)  
67 [arxiv.org/abs/2509.11620](http://arxiv.org/abs/2509.11620). arXiv:2509.11620  
68 [cs].  
69
- 70 Liu, J., Liu, G., Liang, J., Li, Y., Liu, J., Wang,  
71 X., Wan, P., Zhang, D., and Ouyang, W. Flow-  
72 GRPO: Training Flow Matching Models via Online RL,  
73 July 2025. URL [http://arxiv.org/abs/2505.](http://arxiv.org/abs/2505.05470)  
74 [05470](http://arxiv.org/abs/2505.05470). arXiv:2505.05470 [cs].  
75
- 76 Ma, Y., Shui, Y., Wu, X., Sun, K., and Li, H. HPSv3:  
77 Towards Wide-Spectrum Human Preference Score, Au-  
78 gust 2025. URL [http://arxiv.org/abs/2508.](http://arxiv.org/abs/2508.03789)  
79 [03789](http://arxiv.org/abs/2508.03789). arXiv:2508.03789 [cs].  
80
- 81 Maerten, A.-S., Chen, L.-W., De Winter, S., Bossens, C.,  
82 and Wagemans, J. LAPIS: A novel dataset for personal-  
83 ized image aesthetic assessment, 2025. URL [https:](https://arxiv.org/abs/2504.07670)  
84 [//arxiv.org/abs/2504.07670](https://arxiv.org/abs/2504.07670). Version Num-  
85 ber: 1.  
86
- 87 McHugh, M. L. Interrater reliability: the kappa statistic.  
88 *Biochemia Medica*, 22(3):276–282, October 2012. ISSN  
89 1330-0962. URL [https://www.ncbi.nlm.nih.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3900052/)  
90 [gov/pmc/articles/PMC3900052/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3900052/).  
91
- 92 Mehta, M. and Buntain, C. Emotional Images: Assessing  
93 Emotions in Images and Potential Biases in Generative  
94 Models, December 2024. URL [http://arxiv.org/](http://arxiv.org/abs/2411.05985)  
95 [abs/2411.05985](http://arxiv.org/abs/2411.05985). arXiv:2411.05985 [cs].  
96
- 97 Mordvintsev, A., Olah, C., and Tyka, M. Incep-  
98 tionism: Going Deeper into Neural Networks.  
99 URL [https://research.google/blog/](https://research.google/blog/inceptionism-going-deeper-into-neural-networks/)  
100 [inceptionism-going-deeper-into-neural-networks/](https://research.google/blog/inceptionism-going-deeper-into-neural-networks/).  
101
- 102 Peng, Y.-H., Bigham, J. P., and Wu, J. DesignPref: Cap-  
103 turing Personal Preferences in Visual Design Generation,  
104 November 2025. URL [http://arxiv.org/abs/](http://arxiv.org/abs/2511.20513)  
105 [2511.20513](http://arxiv.org/abs/2511.20513). arXiv:2511.20513 [cs].  
106

 Rest of paper (reference and Appendix) is removed.