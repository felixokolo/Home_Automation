package com.example.agile_control;

import android.os.AsyncTask;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class ConnectionSetup extends AsyncTask<String, String, String> {

	@Override
	protected String doInBackground(String... params) {


		OkHttpClient client = new OkHttpClient();
		Request request = new Request.Builder().url(params[0]).build();
		String resp = "null";
		try {
			Response response = client.newCall(request).execute();
			resp = response.body().string();
		}  catch (IOException e) {
			e.printStackTrace();
		}
		return resp;
	}

	@Override
	protected void onPostExecute(String res) {
		super.onPostExecute(res);
	}
}
