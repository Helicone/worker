To run this on any machine with a suitable GPU run.

```bash
sudo docker run -it --gpus=all --env API_KEY=<API_KEY> --env PROMPT_ZERO_URL=https://www.promptzero.com chitalian/promptzero-worker:0.0.1 bash -c "conda run --no-capture-output -n ldm python main.py"
```


# Building Docker
Make sure you have the weights files downloaded here: `weights/sd-v1-4.ckpt`
You can download them here https://huggingface.co/CompVis/stable-diffusion-v-1-4-original

then run docker build...
`docker build . -t chitalian/promptzero-worker:0.0.2`