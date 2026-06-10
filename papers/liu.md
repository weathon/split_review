

{0}------------------------------------------------

# Hi-Light: A Path to High-fidelity, High-resolution Video Relighting With A Refined Evaluation Paradigm

Xiangrui Liu<sup>1</sup>, Haoxiang Li<sup>2</sup>, Yezhou Yang<sup>1</sup>

<sup>1</sup>Arizona State University, <sup>2</sup>Pixocial Technology

<sup>1</sup>{xiangrui, yz.yang}@asu.edu, <sup>2</sup>haoxiang.li@pixocial.com

## Abstract

Video relighting offers immense creative potential and commercial value but is hindered by challenges, including the absence of an adequate evaluation metric, severe light flickering, and the degradation of fine-grained details during editing. To overcome these challenges, we introduce Hi-Light, a novel, plug-and-play framework for high-fidelity, high-resolution, robust video relighting. Our approach introduces three technical innovations: lightness prior anchored guided relighting diffusion that stabilises intermediate relit video, a Hybrid Motion-Adaptive Lighting Smoothing Filter that leverages optical flow to ensure temporal stability without introducing motion blur, and a LAB-based Detail Fusion module that preserves high-frequency detail information from the original video. Furthermore, to address the critical gap in evaluation, we propose the Light Stability Score, the first quantitative metric designed to specifically measure lighting consistency. Extensive experiments demonstrate that Hi-Light significantly outperforms state-of-the-art methods in both qualitative and quantitative comparisons, producing stable, highly detailed relit videos. The codes and demo can be found at [github.com/lxrswdd/Hi-Light](https://github.com/lxrswdd/Hi-Light).

## 1. Introduction

“Lighting is the blank page. It’s the canvas. It’s the thing that you start with — you can’t do anything until you have a light.” — Sir Roger Deakins

Lighting and its interaction with the environment shape how we perceive the world. Manipulating the light can dramatically alter the narrative and emotion buried in the visual media, making it a task of significant aesthetic and commercial value and a long-standing research problem in computer vision. However, video relighting remains a less explored and substantially more challenging domain. As shown in Figure 2, traditional video editing techniques, such as applying filters, are insufficient for this task. While

![Figure 1: Demonstrations of the text-conditioned video relighting task. The figure shows two rows of video frames. The top row shows a sea gull on a wooden pole, with the original input video on the left and the relit video frames on the right, featuring a sunset lighting effect. The bottom row shows a woman drinking coffee, with the original input video on the left and the relit video frames on the right, featuring a green aurora light effect. Captions below each row read: 'A sea gull on a wooden pole, sunset lighting' and 'A woman drinking coffee, green aurora light'.](d3294dc879b451b369c0b06f42e9b39f_img.jpg)

Figure 1: Demonstrations of the text-conditioned video relighting task. The figure shows two rows of video frames. The top row shows a sea gull on a wooden pole, with the original input video on the left and the relit video frames on the right, featuring a sunset lighting effect. The bottom row shows a woman drinking coffee, with the original input video on the left and the relit video frames on the right, featuring a green aurora light effect. Captions below each row read: 'A sea gull on a wooden pole, sunset lighting' and 'A woman drinking coffee, green aurora light'.

Figure 1. Demonstrations of the text-conditioned video relighting task by our framework.

these filters can perform global adjustments to colour and saturation, they cannot synthesize the complex, physically grounded effects of true illumination. Specifically, they fail to model crucial light properties such as directionality, high-lights and shadows [2], or project lighting onto grayscale scenes effectively.

Diffusion models have driven major progress in image generation and editing, spurring rapid advances in data-driven image relighting. Models such as IC-Light [18] now define the state-of-the-art (SOTA). While image relighting leverages large-scale datasets with paired lighting conditions, such data is infeasible for video due to the cost of capturing dynamic scenes under multiple controlled illuminations. Light stage systems [4] provide the closest alternative but require specialised equipment and capture primarily human subjects under simulated lighting, not real-world settings. This scarcity limits direct large-scale video

{1}------------------------------------------------

training and necessitates more complex solutions. Existing approaches, including a recent breakthrough like Light-A-Video [21], still suffer from the following three weaknesses.

**Detail degradation:** The reconstruction process within current video diffusion backbones is often imperfect, leading to a loss of high-frequency details. This causes sharp, fine-grained elements such as foliage and hair to become blurred or smoothed in the relit output. **Light flickering:** The existing solutions [10, 21] generally adopt IC-Light as the relighting model, and when single-image relighting models are applied on a per-frame basis, the resulting video often exhibits severe flicker. This lack of temporal coherence is a major artefact that jeopardises the quality of the final output. **Inadequate evaluation metrics:** Current evaluation methods are restricted to per-frame image metrics and subjective human evaluation. Standard metrics like FID and CLIP score are not able to capture the subtle degradation of fine-grained details. While human evaluation can be more accurate, its small sample size, potential for bias, and lack of scalability make it impractical for comprehensive benchmarking. Notably, there is no established metric designed to quantitatively measure the light flickering problem.

To tackle these challenges, we introduce Hi-Light, a training-free framework that decouples relighting from detail preservation. Hi-Light generates a smoothed, low-resolution relit video and then intelligently projects the new lighting onto the original high-resolution frames, preserving fine-grained details while ensuring light stability. Our framework’s training-free design circumvents the need for large-scale datasets and costly training of new architectures by leveraging computer vision principles to surgically correct the common flickering and detail-loss artefacts of existing SOTA models. To address the evaluation gap, we also propose a new quantitative metric that jointly measures detail preservation and light stability. Our main contributions are:

- We present Hi-Light, a training-free, backbone-agnostic video relighting framework. Hi-Light is the only method capable of processing high-resolution video with computational efficiency, thereby extending accessibility to a wider community of users.
- We introduce a lightness-prior-anchored progressive fusion scheme that suppresses luminance oscillations during diffusion, and two plug-and-play modules: Hybrid Motion-Adaptive Light Smoothing Filter (HMA-LSF) to remove flicker, and LAB Detail-Preserving Fusion (LAB-DF) to restore fine-grained texture.
- We further propose a principled evaluation paradigm for video relighting, including a Light Stability Score ( $S_{LS}$ ) that complements standard fidelity metrics.
- Compared to the second-best method, our approach achieves 80% improvement in light stability and 56% im-

![Figure 2: Comparison of the relighting effects of CapCut Sunset filters and our model. The figure shows a sequence of five frames. The first frame is labeled 'Input Video' and shows a person on a boat. The next three frames are labeled 'CapCut Filters' and show the same scene with different, somewhat artificial color casts (orange, purple, blue). The final frame is labeled 'Hi-Light Relit (ours)' and shows the scene with natural, smooth lighting transitions.](d5fc881e4328d6a2e76c9576408ced49_img.jpg)

Figure 2: Comparison of the relighting effects of CapCut Sunset filters and our model. The figure shows a sequence of five frames. The first frame is labeled 'Input Video' and shows a person on a boat. The next three frames are labeled 'CapCut Filters' and show the same scene with different, somewhat artificial color casts (orange, purple, blue). The final frame is labeled 'Hi-Light Relit (ours)' and shows the scene with natural, smooth lighting transitions.

Figure 2. Comparison of the relighting effects of CapCut Sunset filters and our model.

provement in detail preservation, setting the new SOTA.

## 2. Related Work

**Visual Media Relighting** Controlling illumination is a fundamental challenge in computer vision [3], with extensive research dedicated to single-image relighting. Early deep learning approaches made significant strides, particularly in portrait relighting [8, 11]. To tackle this, existing methods have explored various strategies. Some approaches rely on explicit 3D geometry and reflectance estimation. For example, SunStage [14] performs test-time optimization on a selfie video to reconstruct facial properties, while IllumiCraft [9] jointly models lighting and geometry using environment maps and 3D point tracks. Other works focus on disentanglement; LuminSculpt [20] employs a network trained on synthetic data to decouple illumination from other scene factors. TC-Light [10] first aligns global exposure using a per-frame appearance embedding; subsequently, it refines fine-grained illumination and texture by optimizing a canonical representation called the Unique Video Tensor. Setting the new state-of-the-art, Light-A-Video [21] recently introduced a training-free framework that adopts a progressive light fusion method to strengthen the temporal consistency in the denoising process.

**Reference-Based Video Quality Assessment** For conditional generation tasks such as video-to-video translation or restoration, where a ground-truth reference exists, a variety of full-reference metrics are utilised. The most fundamental method is the Peak Signal-to-Noise Ratio (PSNR), which is based on simple mean squared error but often correlates poorly with human perception. A significant advancement was the Structural Similarity Index (SSIM), which provides a more perceptually relevant measure by comparing luminance, contrast, and structure [16]. This was further improved by the Multi-Scale SSIM (MS-SSIM), which evaluates these properties across multiple resolutions for more robust results [15]. To better align with human visual judgment, modern metrics leverage deep learning. The Learned

{2}------------------------------------------------

Perceptual Image Patch Similarity (LPIPS) pioneered this by using features from deep networks to effectively predict perceptual similarity [19]. These assessments focused on the video details, while the lighting quality was generally missing; only small human evaluations have been done, but it is highly subjective and lacks consistency and scientific robustness [10, 21].

## 3. Methodology

### 3.1. Relighting Evaluation

A critical challenge in video relighting is the lack of an evaluation protocol that can simultaneously assess the two primary weaknesses of existing methods: temporal instability (light flickering) and the degradation of high-frequency details. To address this gap, we establish a new evaluation paradigm, Relit Video Evaluation. In the following subsections, we introduce a novel Light Stability Score to quantitatively measure light flickering and adopt the Structural Similarity Index (SSIM) to evaluate detail preservation.

#### 3.1.1. Light Stability Score

The light flickering problem persists in all the existing work; therefore, it is important to propose a way to measure the stability of the lighting effect. First, to quantify temporal brightness dynamics from video data, each frame is converted to grayscale. A brightness threshold,  $\tau$ , is applied to segment each frame, yielding a set of suprathreshold pixels,  $P_t$ , which are the bright pixels that are susceptible to the flicker problem. Two time series signals are derived from this set: the average intensity of bright pixels  $I_t$  and the number of bright pixels  $C_t$ . A third signal, representing the frame-to-frame change in average intensity, is derived by taking the first derivative of the  $I_t$  series,  $\dot{I}_t$ .

Next, a quantitative smoothness score,  $S$ , is calculated for each of the three time series signals to assess the video’s light fluctuation. This score is based on the magnitude of frame-to-frame changes relative to the signal’s overall dynamic range. Given a series of video frames,  $t = \{t_1, t_2, \dots, t_N\}$ , the mean absolute change,  $M$ , is first computed as  $M = \frac{1}{N-1} \sum_{i=0}^{N-2} |t_{i+1} - t_i|$ . This value is then normalized by the signal’s peak-to-peak range,  $R = \max(t) - \min(t)$ , yielding a scale-invariant unsmoothness metric  $U_{\text{norm}} = \frac{M}{R}$ . Next, an exponential decay function transforms this metric into a final score,  $S$ , bounded by 0 and 1; a higher score denotes greater smoothness. Finally, the Light Stability Score,  $S_{LS}$ , will be the average of the scores:  $S_{LS} = \frac{S_{I_t} + S_{C_t} + S_{\dot{I}_t}}{3}$ .

#### 3.1.2. Detail Preservation

Existing relit videos suffer from detail loss during the diffusion process. To measure how many details are preserved in the relit video, we propose using the Structural Similarity Index (SSIM), which mimics how the human visual system

works. Instead of just comparing individual pixels, SSIM evaluates the similarity of local patches of a frame based on three key components: luminance, contrast, and structure. The structure comparison is the most crucial component for evaluating the similarity of the details of videos; it compares the underlying shapes, textures, and patterns within the patches. The formulation of SSIM is as follows:

$$Q(i, j) = \frac{2\mu_1(i, j)\mu_2(i, j) + C_1}{\mu_1^2(i, j) + \mu_2^2(i, j) + C_1} \times \frac{2\sigma_1(i, j)\sigma_2(i, j) + C_2}{\sigma_1^2(i, j) + \sigma_2^2(i, j) + C_2} \times \frac{\sigma_{12} + C_3}{\sigma_1(i, j) + \sigma_2(i, j) + C_3}, \quad (1)$$

$$SSIM(I_1, I_2) = \frac{1}{MN} \sum_{i=1}^M \sum_{j=1}^N Q(i, j), \quad (2)$$

where  $Q$  is the local quality score,  $\mu_1$  and  $\mu_2$  are the local means,  $\sigma_1$  and  $\sigma_2$  are the standard deviation, and  $\sigma_{12}$  is the correlation of the frames  $I_1$  and  $I_2$ .  $C_1$ ,  $C_2$ , and  $C_3$  are the saturation constants. While multi-scale SSIM may perform better in general at the expense of computational resources and efficiency, we are only concerned with fidelity, regardless of colour, so SSIM is a better choice.

### 3.2. Hi-Light

To bridge this crucial gap between temporal coherence and visual fidelity, we introduce the Hi-Light video relighting framework as shown in the Figure 3. The video is first downsampled to  $480p$  resolution. This step is necessary to utilize diffusion models trained at this resolution and reduces computational requirements (e.g., enabling inference on a single GPU). The downsampled video will then go through the guided relighting diffusion loop in the generation backbone to obtain an intermediate relit video, which possesses the relighting information but suffers from detail degradation and flickering light. The flicker light problem will then be handled by a Hybrid Motion-Adaptive Lighting Smoothing Filter, which is specifically designed to eliminate the flicker artifacts inherent in frame-by-frame generative processes. Finally, our novel LAB Detail-Preserve Fusion (LAB-DF) module intelligently transfers the stabilized lighting from the smoothed video onto the original high-resolution source video, preserving the high-frequency details.

#### 3.2.1. Progressive Light Fusion Guided Diffusion with lightness Prior anchored

Directly applying an image relighting model results in inter-frame inconsistency. In the CIE LAB colour space [1], the  $L$  channel encodes the perceptual lightness information — a monotone transform of scene luminance. Light flickering in the video relighting task manifests predominantly as low-

{3}------------------------------------------------

![Figure 3: The overall structure of the Hi-Light framework. The diagram shows a flow from 'High Resolution Video Input (I_HR)' through 'Down sampling' to a 'Guided Relighting Diffusion' module. This module takes a 'Text prompt: "morning sun light"' and a 'Lightness Prior' as input. It processes frames from t=0 to t=T-1 using 'IC - Light' and 'Guided diffusion' to produce 'I_int'. This intermediate output is then processed by a 'Hybrid Motion-adaptive Lighting Smoothing Filter (HMA-LSF)' which includes 'Int. Relit Video', 'Optical Flow Filter', and 'Bilateral Filter' to produce 'I_smooth'. Finally, the 'LAB Detail-Preserve Fusion (LAB-DF)' module combines 'I_smooth' and 'LAB Feature Maps' to produce the 'High Resolution Relit Video' (I_out = LAB-DF(I_HR, I_smooth)).](2763901b7a1fd1b5d704cdc450d12ed0_img.jpg)

Figure 3: The overall structure of the Hi-Light framework. The diagram shows a flow from 'High Resolution Video Input (I\_HR)' through 'Down sampling' to a 'Guided Relighting Diffusion' module. This module takes a 'Text prompt: "morning sun light"' and a 'Lightness Prior' as input. It processes frames from t=0 to t=T-1 using 'IC - Light' and 'Guided diffusion' to produce 'I\_int'. This intermediate output is then processed by a 'Hybrid Motion-adaptive Lighting Smoothing Filter (HMA-LSF)' which includes 'Int. Relit Video', 'Optical Flow Filter', and 'Bilateral Filter' to produce 'I\_smooth'. Finally, the 'LAB Detail-Preserve Fusion (LAB-DF)' module combines 'I\_smooth' and 'LAB Feature Maps' to produce the 'High Resolution Relit Video' (I\_out = LAB-DF(I\_HR, I\_smooth)).

Figure 3. The overall structure of our Hi-Light framework. The framework first processes a downsampled video through a guided relighting diffusion loop to generate lighting information where a lightness prior is anchored. The intermediate output is then stabilized using an HMA-LSF to eliminate flickering. Finally, the LAB-DF module transfers the illumination information to the high-resolution source.

to mid-frequency oscillations in the  $L$  channel. Building on progressive light fusion [21], we additionally inject a *per-step lightness prior* to damp luminance oscillations across the frames. We first define a high-pass lighting residual; let  $I^{\text{in}}$  be the input video at  $t=0$  which is a stable reference point. Define a static lightness residual by preserving the high-frequency information in the  $L$  channel of  $I^{\text{in}}$  using a Gaussian filter  $G_\sigma$ :

$$\begin{aligned} \Delta L &= L(I^{\text{in}}) - (G_\sigma * L(I^{\text{in}})), \\ G_\sigma(x, y) &= \frac{1}{2\pi\sigma^2} \exp\left(-\frac{x^2 + y^2}{2\sigma^2}\right). \end{aligned} \quad (3)$$

The lightness residual  $L - G_\sigma * L$  is preferred over raw gradients or a Laplacian transform because it is DC-insensitive and less noise-amplifying at very high frequencies due to the bounded gain  $1 - \widehat{G}_\sigma(\omega)$ , which is important for temporal stability. Then add the static lightness residual  $\Delta L$  with empirically yielded fixed strength  $\gamma = 0.3$ :

$$L_t \leftarrow L_t + \gamma \Delta L, \quad (4)$$

which maintain a time-invariant anchor in the  $L$  channel, reducing frame-to-frame variance in lighted regions and thus

increasing stability. Because  $\int \Delta L \approx 0$  (mean-free under normalized  $G_\sigma$ ), this addition minimally perturbs global brightness, avoiding drift.

At diffusion step  $t$ , we form the fused input as in progressive light fusion and denoise:

$$\begin{aligned} I_t^f &= I_t^c + \lambda_t (I_t^c - \tilde{I}_t^r), \\ I_{t+1}^f &= \mathcal{D}_\theta(I_t^f), \end{aligned} \quad (5)$$

where the weight  $\lambda_t$  is a gradually decreasing weight. This formulation initially emphasizes the influence of the relit target  $\tilde{I}_t^r$ , providing strong guidance in the early steps. As  $\lambda_t$  decays, the process shifts toward refinement by the diffusion model, reducing dependency on the relit signal. The fused target at step  $t$  is fed to the denoiser  $\mathcal{D}_\theta(\cdot)$  to produce the next consistent state, thereby refining the denoising trajectory.

#### 3.2.2. Hybrid Motion-Adaptive Lighting Smoothing Filter (HMA-LSF)

A simple temporal smoother that averages frames may result in blurriness, especially for moving objects. To stabilise the light flickering problem, we design a novel hybrid temporal smoothing filter that adaptively integrates op-

{4}------------------------------------------------

tical-flow-based motion compensation with bilateral filtering. Unlike prior temporal smoothers, which either blur motion or leave residual flicker, our design couples flow-based alignment with spatial edge-aware filtering, explicitly targeting the two dominant flicker sources: motion misalignment and compression noise.

![Figure 4: LAB feature maps extraction and fusion process. The diagram shows the flow from 'Input Video' and 'Intermediate Relit Video' through 'Feature Extraction' to produce 'High-frequency detail' and 'Illumination Information'. These are then fused into a 'LAB-DF fused video'. The fused video is shown in 'L Channel', 'A Channel', and 'B Channel' components.](690fce4fb5c9cbb8beb560cb2a3fcbeb_img.jpg)

The diagram illustrates the LAB feature maps extraction and fusion process. It starts with an 'Input Video' and an 'Intermediate Relit Video'. Both undergo 'Feature Extraction' to produce 'High-frequency detail' and 'Illumination Information'. These two components are then fused into a 'LAB-DF fused video'. The fused video is shown in three channels: 'L Channel', 'A Channel', and 'B Channel'.

Figure 4: LAB feature maps extraction and fusion process. The diagram shows the flow from 'Input Video' and 'Intermediate Relit Video' through 'Feature Extraction' to produce 'High-frequency detail' and 'Illumination Information'. These are then fused into a 'LAB-DF fused video'. The fused video is shown in 'L Channel', 'A Channel', and 'B Channel' components.

Figure 4. LAB feature maps will be extracted from the intermediate relit video and the input video. The high-frequency information from the input video will be fused with the illumination information from the intermediate relit video.

**Optical Flow Light Smoothing Filter** The main objective of the optical flow filter is to distinguish two types of brightness changes: Legitimate change, which is when an object gets brighter or darker, or a bright object moves to a new location, and illegitimate change (light flickering), where pixels' brightness fluctuates rapidly and erratically from one frame to the next. Optical flow is the estimation of the motion of pixels between two consecutive frames. The filter will calculate a motion vector for every pixel in the frame, which is important for identifying moving objects. The equation for the optical flow constraint is given by:

$$I(x, y, t) = I(x + \delta x, y + \delta y, t + \delta t), \quad (6)$$

where  $I(x, y, t)$  is the pixel intensity at position  $(x, y)$  at time  $t$  and the goal is to find the displacement  $(\delta x, \delta y)$ . Upon obtaining the flow, the filter performs motion compensation by taking the previously smoothed frame and warping it according to the calculated motion vectors. This warping aligns the content of the previous smoothed frame with the content of the current frame. The result is an estimate of what the previous smoothed frame would look like if the objects had moved to their new positions in the current frame. To address the flicker pixels, the filter blends the warped (motion-compensated) frame  $f_{t-1}$  with the current frame  $f_t$ , and the blending is controlled by a weighted sum of the two frames as follows:

$$f_{blend} = \alpha f_{warped} + (1 - \alpha) f_t. \quad (7)$$

To avoid motion blur in fast-moving scenes, the  $\alpha$  term is adaptive to the magnitude of motion. When motion is high, it reduces the  $\alpha$  value, thereby relying more on the current frame and reducing the smoothing effect. This effectively prevents ghostly trails behind moving objects. Moreover, the change between two consecutive frames may be negligible, so we introduce a frame window; instead of just considering the immediately preceding frame, we calculate a weighted average of a window of frames, giving more importance to the most recent ones. This provides a more robust history of the pixel values, improving the smoother results.

Instead of adopting transformer-based optical flow models like RAFT [12], which demands over 80GB of VRAM for 81 video frames, we utilize the Farneback optical flow via the OpenCV library. This CPU-only approach is computationally friendly, ensuring broader user accessibility.

**Bilateral Filter** The bilateral filter is a non-linear, edge-preserving smoothing filter. For each pixel  $p$ , it calculates a weighted average of its surrounding pixels, and the weight depends on spatial distance and intensity difference:

$$BF[I]_p = \frac{1}{W_p} \sum_{q \in SW} G_{\sigma_s}(\|p - q\|) G_{\sigma_r}(|I_p - I_q|) \cdot I_q. \quad (8)$$

$p$  and  $q$  are the target pixel and its neighbour pixels within the search window  $SW$ ,  $I$  denotes the intensity,  $G$  is the Gaussian kernel, and  $W_p$  is the normalisation factor that constrains the intensity value. A neighbouring pixel is assigned a low weight if it is either too far away or if its intensity is very different from the central pixel. When the filter is over a flat region, the intensity differences are small, so the range weights are high. The filter acts like a standard blur, smoothing out noise. When the filter crosses a sharp edge, the intensity differences become large. The weights for pixels on the other side of the edge drop to near zero, effectively ignoring them. This preserves the sharpness of the edge while still smoothing the areas on either side of it. To sum up, the optical flow filter tracks moving objects to smooth out inconsistent brightness fluctuations from one frame to the next and smooth the flicker intelligently. Then the bilateral filter reduces any remaining spatial noise, such as compression artefacts and inconsistent colour in flat regions.

#### 3.2.3. LAB Detail-Preserve Fusion (LAB-DF)

As shown in Fig. 4, we convert frames to CIE LAB, where  $L$  channel encodes perceptual lightness and  $A$  and  $B$  channels encode colour. A direct approach is copying the input's high-frequency  $L$  into the relit video which does preserve details, but it introduces afterimages (ghosting). The afterimage problem is that the VDM can not reproduce geometry and edges exactly, so injecting fine-grained information

{5}------------------------------------------------

![Figure 5: A visual comparison of relighting methods. The top row shows five frames of a building at sunset, with a dotted red box highlighting a region of contrast. The bottom row shows the same region enlarged for five methods: TC-Light, LAV (AnimateDiff), LAV (CogVideoX), LAV (Wan), and Hi-Light (ours). Hi-Light shows the best detail preservation.](440e59dae4772c0152116a3abd34331a_img.jpg)

Figure 5: A visual comparison of relighting methods. The top row shows five frames of a building at sunset, with a dotted red box highlighting a region of contrast. The bottom row shows the same region enlarged for five methods: TC-Light, LAV (AnimateDiff), LAV (CogVideoX), LAV (Wan), and Hi-Light (ours). Hi-Light shows the best detail preservation.

Figure 5. A visual comparison of relighting methods with the text prompt “sunset lighting.” Hi-Light achieves the best detail preservation. The top row shows a relit video frame, while the dotted red box marks regions of contrast, enlarged in the bottom row.

from the input frame into a misaligned relit frame accumulates residuals.

To avoid afterimage, we invert the transfer: we take only the low-frequency illumination from the relit lightness and add it to the input lightness. Concretely,

$$L' = L_i + \beta (G_\sigma * L_r), \quad (9)$$

where  $L_i$  and  $L_r$  are the input and relit  $L$  channels,  $G_\sigma$  removes structural information from  $L_r$ , retaining exposure/contrast and light direction, and  $\beta \in [0, 1]$  controls the transfer strength. We then combine the enhanced lightness with the relit chroma  $A$  and  $B$  channels to retain the intended colour of the new lighting:

$$V'(x, y) = [L'(x, y), A_r(x, y), B_r(x, y)]. \quad (10)$$

This design effectively eliminates the afterimage problem, preserves the input’s textures, and carries over the relit scene’s colour and tonal style.

## 4. Experiment

**Baseline** Given that the research in video generation and editing is relatively new, there is a shortage of video relighting work. We have conducted experiments using the open-source SOTA model Light-A-Video [21] with its three different VDM backbones (CogVideoX [17], AnimateDiff [5], and Wan [13]) and TC-Light [10]. The configuration of the baseline models is the same as their demonstration configuration.

**Experiment Setup** We conducted a rigorous comparative experiment where we used 100 video clips (70 human portraits, 30 non-human environments), collected from the internet and self-recorded. The video content spans diverse scenarios, including indoor and outdoor environments, as well as relatively static and highly dynamic scenes. The clips range from 1080p to 2160p and were standardised to 81 frames at 24 fps. Following the baselines, Hi-Light applies 30% noise to the input latent, with the VDM performing denoising over  $T_m = 25$  steps to produce intermediate relit videos. The fusion weight is set as  $\lambda_t = 1 - t/T_m$ . Empirical tests determined amplification factors of 20, 20, and 5 for  $S_L, S_C, S_I$ , respectively, to balance magnitudes. The hyperparameters were fixed for all the comparative experiments. The lighting prompts include: aurora light, reading lamp light, natural light, sunset light, morning light, dawn lighting, snowy winter lighting, light coming through a window, neon light, and torch flame light. The directions of light include: top, bottom, left, and right. The experiments were conducted using one L40 GPU.

## 5. Results

We conduct a comprehensive evaluation of Hi-Light, comparing it against open-source SOTA methods across qualitative, quantitative, and signal-processing domains to validate its effectiveness. We first present a qualitative comparison in Figure 5, showcasing frames from a relit video. Competing methods like TC-Light produce a washed-out effect, while the LAV variants suffer from significant detail degradation, resulting in blurry textures on the building and

{6}------------------------------------------------

| Model | SSIM ( $\uparrow$ ) | LPIPS ( $\downarrow$ ) | FID ( $\downarrow$ ) | VBench ( $\uparrow$ ) | $S_{LS}$ ( $\uparrow$ ) |
|-|-|-|-|-|-|
| TC-Light [10] | 0.484 | 0.464 | 120 | 0.718 | 0.281 |
| LAV (AnimateDiff) [21] | 0.552 | 0.434 | 241 | 0.714 | 0.098 |
| LAV (CogVideoX) [21] | 0.597 | 0.402 | 133 | 0.736 | 0.267 |
| LAV (Wan) [21] | 0.604 | 0.395 | 135 | 0.728 | 0.279 |
| Hi-Light (ours) | <b>0.943</b> | <b>0.247</b> | <b>76</b> | <b>0.736</b> | <b>0.509</b> |

Table 1. Quantified results of the video relighting models.

foreground foliage. In contrast, Hi-Light renders the new lighting with sharp highlights, while preserving the original high-frequency details.

To quantify these visual improvements, we evaluate all methods across multiple dimensions: SSIM, LPIPS, Fr chet Inception Distance (FID),  $S_{LS}$ , and an average score of VBench. The scatter plot in Figure 6 provides an intuitive visualization of Hi-Light’s superior performance. Our method is positioned in the top-right quadrant, indicating both high detail fidelity and robust lighting stability. It is notably close to the original input video, which represents the ideal target for these metrics.

The numerical breakdown in Table 1 reinforces this conclusion. Hi-Light achieves an SSIM of 0.943, significantly outperforming the next best method, LAV (Wan), which scores 0.604. This substantial margin highlights our framework’s exceptional ability to preserve high-frequency details while relighting. Beyond detail preservation, Hi-Light demonstrates superior generative quality and consistency, achieving the lowest FID (76) and LPIPS (0.247) scores, as well as the highest VBench score (0.736). Furthermore, Hi-Light attains an overall Light Stability Score ( $S_{LS}$ ) of 0.509, nearly doubling the performance of competing methods like TC-Light (0.281). This quantitative evidence conclusively demonstrates that Hi-Light sets a new SOTA standard, uniquely capable of achieving stable, high-fidelity video relighting. For a comprehensive performance breakdown, including complete VBench sub-metrics and expanded comparisons, please refer to Appendix A.1.

To further understand the underlying reasons for this performance, we analyze the outputs in the frequency and temporal domains (Figure 7). The frequency analysis on the left provides strong evidence for Hi-Light’s detail preservation capability. The Fourier spectra of competing methods reveal a pronounced attenuation of high-frequency components, visually confirming a loss of sharpness. In contrast, the spectrum from Hi-Light is nearly indistinguishable from the input’s, proving that our method relights the scene without sacrificing textural information. Simultaneously, the light stability plots on the right validate our approach to eliminating flicker. The “Frame-to-Frame Change in Avg. Bright Pixel Intensity” graph is particularly revealing: competitors exhibit highly erratic fluctuations, a quantitative signature of severe flicker artefacts. Conversely, Hi-

![Figure 6: Video Relighting Performance Plot. A scatter plot comparing SSIM (Y-axis, 0.0 to 1.0) and Light Stability Score (X-axis, 0.0 to 0.7). The plot shows the performance of various methods: Input Video (top right), Hi-Light (ours) (top right), LAV (Wan) (middle right), LAV (CogVideoX) (middle left), TC-Light (bottom left), and LAV (AnimateDiff) (bottom left). Red dashed lines indicate improvements of 56% in SSIM and 80% in Light Stability Score for Hi-Light (ours) compared to the second-best methods.](01da0d212fb571933f10f96556157745_img.jpg)

| Method | Light Stability Score (X) | SSIM (Y) |
|-|-|-|
| Input Video | ~0.68 | ~0.95 |
| Hi-Light (ours) | ~0.51 | ~0.94 |
| LAV (Wan) | ~0.31 | ~0.60 |
| LAV (CogVideoX) | ~0.28 | ~0.55 |
| TC-Light | ~0.28 | ~0.48 |
| LAV (AnimateDiff) | ~0.10 | ~0.55 |

Figure 6: Video Relighting Performance Plot. A scatter plot comparing SSIM (Y-axis, 0.0 to 1.0) and Light Stability Score (X-axis, 0.0 to 0.7). The plot shows the performance of various methods: Input Video (top right), Hi-Light (ours) (top right), LAV (Wan) (middle right), LAV (CogVideoX) (middle left), TC-Light (bottom left), and LAV (AnimateDiff) (bottom left). Red dashed lines indicate improvements of 56% in SSIM and 80% in Light Stability Score for Hi-Light (ours) compared to the second-best methods.

Figure 6. Visualized comparison of methods. Hi-Light outperforms other methods on both SSIM and Light Stability Score, achieving relative improvements of 56% and 80%, respectively, over the second-best methods.

Light maintains a remarkably more stable and smooth profile. These plots directly demonstrate the efficacy of our hybrid motion-adaptive smoothing filter in producing temporally coherent results.

To validate the perceptual relevance of our proposed  $S_{LS}$ , we conducted a double-blind human evaluation with 30 participants, including a computer vision professor, 7 digital art professionals, and 22 graduate students. Participants ranked randomized video sets based on temporal light stability and spatial detail quality. Hi-Light consistently outperformed competing methods, securing the top rank in 95.6% of evaluations for light stability and 91.1% for detail quality (see Appendix A.8). These results confirm Hi-Light’s superior performance and validate  $S_{LS}$  reliability.

## 6. Ablation Study

Starting from the baseline in Table 4, adding the Light-ing Prior alone raises stability modestly with a small SSIM change. Its main effect is on the derivative term  $S_j$ , showing that it damps frame-to-frame light changes. Adding the Smooth Filter on top of the prior delivers the largest stability gain, pushing  $S_{LS}$  to 0.462, while fidelity stays simi-

{7}------------------------------------------------

![Figure 7: Comparison of video relighting methods. Left: Frequency magnitude spectra for Input Video, Hi-Light (ours), LAV (AnimateDiff), TC-Light, LAV (Wan), and LAV (CogVideoX). Right: Three smoothness scores over time (0 to 0.4s). Top: Average Intensity of Bright Pixels Over Time (Threshold > 125). Middle: Number of Bright Pixels Over Time (Threshold > 125). Bottom: Frame-to-frame Change in Avg. Bright Pixel Intensity. Legend: Input Video (green), LAV (Wan) (orange), TC-Light (blue), Hi-Light (ours) (purple).](c3c305cefbac2e7b13be34ab87054d1e_img.jpg)

Figure 7: Comparison of video relighting methods. Left: Frequency magnitude spectra for Input Video, Hi-Light (ours), LAV (AnimateDiff), TC-Light, LAV (Wan), and LAV (CogVideoX). Right: Three smoothness scores over time (0 to 0.4s). Top: Average Intensity of Bright Pixels Over Time (Threshold > 125). Middle: Number of Bright Pixels Over Time (Threshold > 125). Bottom: Frame-to-frame Change in Avg. Bright Pixel Intensity. Legend: Input Video (green), LAV (Wan) (orange), TC-Light (blue), Hi-Light (ours) (purple).

Figure 7. **Left** shows the frequency magnitude spectra. Our edited video has an identical-looking spectrum to the original video, suggesting that it retains most of the fine-grained details. Meanwhile, the other baselines have a more concentrated spread resulting from detail degradation. **Right** shows the three smoothness scores. Plot for TC-Light is shorter as it has 30 frames. For plot clarity, only LAV (Wan) is included here; the complete plots can be found in Appendix A.2.

| Method |  |  | SSIM ( $\uparrow$ ) | $S_{LS}$ ( $\uparrow$ ) |
|-|-|-|-|-|
| LAB-DF | HMA-LSF | Lighting Prior |  |  |
| $\times$ | $\times$ | $\times$ | 0.607 | 0.285 |
| $\times$ | $\times$ | $\checkmark$ | 0.615 | 0.353 |
| $\times$ | $\checkmark$ | $\times$ | 0.612 | 0.462 |
| $\times$ | $\checkmark$ | $\checkmark$ | 0.623 | 0.476 |
| $\checkmark$ | $\checkmark$ | $\checkmark$ | <b>0.943</b> | <b>0.509</b> |

Table 2. Ablation study result on our methodology.

lar—this module is the key driver of temporal smoothness. Pairing the Lighting Prior with LAB-DF instead yields a large jump in SSIM (0.939) with moderate stability gains, confirming that LAB-DF is the chief detail-preserving component. Combining all three gives the best of both: the highest SSIM and the strongest overall stability. Appendix A.2 contains a comprehensive and detailed ablation study focusing on architecture, efficiency, VDM backbone, number of time steps, and noise strength.

## 7. Conclusion

In this work, we addressed the key challenges of detail degradation and the light flickering problem in video relighting. We introduced Hi-Light, a novel training-free

framework that successfully generates high-fidelity and flicker-free relit videos. Our primary contributions include a lightness prior anchored diffusion scheme and a novel HMA-LSF that ensures temporal coherence and a LAB-DF module that preserves fine-grained details with remarkable fidelity. We also proposed the Light Stability Score, a new quantitative metric to standardise the evaluation of lighting stability, a critical but previously overlooked aspect of the task. Through comprehensive experiments, we have shown that Hi-Light significantly surpasses existing SOTA methods, establishing a new benchmark for quality and robustness in video relighting and opening up new possibilities for creative video editing. Our methodology can be extended to broader video editing by anchoring task-specific attribute priors (e.g. texture, style, colour), applying the same progressive residual to edit a long, temporally consistent video.

## References

- [1] *Colorimetry*. Number 15.2 in CIE Publication. Commission Internationale de l’Éclairage, Vienna, Austria, 2nd edition, 1976. 3
- [2] Longchao Da, Xiangrui Liu, Mithun Shivakoti, Thirulogasanar Pranav Kutralingam, Yezhou Yang, and Hua Wei. Deepshade: Enable shade simulation by text-conditioned im-

{8}------------------------------------------------

- age generation. *International Joint Conferences on Artificial Intelligence*, 2025. 1
- [3] Longchao Da, Rui Wang, Xiaojian Xu, Parminder Bhatia, Taha Kass-Hout, Hua Wei, and Cao Xiao. Flans: A foundation model for free-form language-based segmentation in medical images. In *Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2*, pages 404–414, 2025. 2
 - [4] Paul Debevec, Tim Hawkins, Chris Tchou, Haarm-Pieter Duiker, Westley Sarokin, and Mark Sagar. Acquiring the reflectance field of a human face. In *Proceedings of the 27th annual conference on Computer graphics and interactive techniques*, pages 145–156, 2000. 1
 - [5] Yuwei Guo, Ceyuan Yang, Anyi Rao, Zhengyang Liang, Yaohui Wang, Yu Qiao, Maneesh Agrawala, Dahua Lin, and Bo Dai. Animatediff: Animate your personalized text-to-image diffusion models without specific tuning. *The Twelfth International Conference on Learning Representations*, 2024. 6, 11
 - [6] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter. Gans trained by a two time-scale update rule converge to a local nash equilibrium. *Advances in neural information processing systems*, 30, 2017. 10
 - [7] Ziqi Huang, Yinan He, Jiashuo Yu, Fan Zhang, Chenyang Si, Yuming Jiang, Yuanhan Zhang, Tianxing Wu, Qingyang Jin, Nattapol Chanpaisit, et al. Vbench: Comprehensive benchmark suite for video generative models. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 21807–21818, 2024. 10
 - [8] Hoon Kim, Minje Jang, Wonjun Yoon, Jisoo Lee, Donghyun Na, and Sanghyun Woo. Switchlight: Co-design of physics-driven architecture and pre-training framework for human portrait relighting. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 25096–25106, 2024. 2
 - [9] Yuanze Lin, Yi-Wen Chen, Yi-Hsuan Tsai, Ronald Clark, and Ming-Hsuan Yang. Illumicraft: Unified geometry and illumination diffusion for controllable video generation. *arXiv preprint arXiv:2506.03150*, 2025. 2
 - [10] Yang Liu, Chuanchen Luo, Zimo Tang, Yingyan Li, Yuran Yang, Yuanyong Ning, Lue Fan, Zhaoxiang Zhang, and Junran Peng. Tc-light: Temporally coherent generative rendering for realistic world transfer. *arXiv preprint arXiv:2506.18904*, 2025. 2, 3, 6, 7, 15
 - [11] Thomas Nestmeyer, Jean-François Lalonde, Iain Matthews, and Andreas Lehrmann. Learning physics-guided face relighting under directional light. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 5124–5133, 2020. 2
 - [12] Zachary Teed and Jia Deng. Raft: Recurrent all-pairs field transforms for optical flow. In *European conference on computer vision*, pages 402–419. Springer, 2020. 5
 - [13] Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao, Chen-Wei Xie, Di Chen, Feiwu Yu, Haiming Zhao, Jianxiao Yang, et al. Wan: Open and advanced large-scale video generative models. *arXiv preprint arXiv:2503.20314*, 2025. 6, 11
 - [14] Yifan Wang, Aleksander Holynski, Xiuming Zhang, and Xuaner Zhang. Sunstage: Portrait reconstruction and relighting using the sun as a light stage. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 20792–20802, 2023. 2
 - [15] Zhou Wang, Eero P Simoncelli, and Alan C Bovik. Multi-scale structural similarity for image quality assessment. In *The thirty-seventh asilomar conference on signals, systems & computers*, 2003, pages 1398–1402. Ieee, 2003. 2
 - [16] Zhou Wang, Alan C Bovik, Hamid R Sheikh, and Eero P Simoncelli. Image quality assessment: from error visibility to structural similarity. *IEEE transactions on image processing*, 13(4):600–612, 2004. 2
 - [17] Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, Jiazheng Xu, Yuanming Yang, Wenyi Hong, Xiaohan Zhang, Guanyu Feng, et al. Cogvideox: Text-to-video diffusion models with an expert transformer. *The Thirteenth International Conference on Learning Representations*, 2025. 6, 11
 - [18] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Scaling in-the-wild training for diffusion-based illumination harmonization and editing by imposing consistent light transport. In *The Thirteenth International Conference on Learning Representations*, 2025. 1
 - [19] Richard Zhang, Phillip Isola, Alexei A Efros, Eli Shechtman, and Oliver Wang. The unreasonable effectiveness of deep features as a perceptual metric. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, pages 586–595, 2018. 3
 - [20] Yuxin Zhang, Dandan Zheng, Biao Gong, Jingdong Chen, Ming Yang, Weiming Dong, and Changsheng Xu. Lumisculpt: A consistency lighting control network for video generation. *arXiv preprint arXiv:2410.22979*, 2024. 2
 - [21] Yujie Zhou, Jiazi Bu, Pengyang Ling, Pan Zhang, Tong Wu, Qidong Huang, Jinsong Li, Xiaoyi Dong, Yuhang Zang, Yuhang Cao, et al. Light-a-video: Training-free video relighting via progressive light fusion. In *International Conference on Computer Vision*, 2025. 2, 3, 4, 6, 7, 10, 15

 Rest of paper (reference and Appendix) is removed.