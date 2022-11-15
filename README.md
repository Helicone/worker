Make sure to first download the Stable Diffusion v1.4 weights to weights/sd-v1-4.ckpt before building the dockerfile. You can do so by first [getting an access token](https://huggingface.co/docs/hub/security-tokens) from HuggingFace, then running
```bash
wget --header="Authorization: Bearer {{hf token}}" https://huggingface.co/CompVis/stable-diffusion-v-1-4-original/resolve/main/sd-v1-4.ckpt
```

Next, build the image with
```bash
sudo docker build -t promptzero-worker .
```


Finally, to run this on any machine with a suitable GPU:

```bash
sudo docker run -it --gpus=all --env API_KEY=<API_KEY> --env PROMPT_ZERO_URL=https://www.promptzero.com chitalian/promptzero-worker:0.0.1 bash -c "conda run --no-capture-output -n ldm python main.py"
```
