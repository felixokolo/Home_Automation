package com.example.agile_control;

import android.content.Context;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.view.WindowManager;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import java.util.concurrent.TimeUnit;

import java.io.IOException;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;


public class Splash extends AppCompatActivity {

    @SuppressWarnings("DEPRECATION")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.R) {
            final WindowInsetsController insetsController = getWindow().getInsetsController();
            if (insetsController != null) {
                insetsController.hide(WindowInsets.Type.statusBars());
            }
        } else {
            getWindow().setFlags(
                    WindowManager.LayoutParams.FLAG_FULLSCREEN,
                    WindowManager.LayoutParams.FLAG_FULLSCREEN
            );
        }
        setContentView(R.layout.activity_splash);
        new ConnectionSetup().execute();


    }

    public class ConnectionSetup extends AsyncTask<Void, Void, Void> {

        String url = "http://192.168.43.72:5000/api/v1/agile/user_1";
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url(url).build();
        @Override
        protected Void doInBackground(Void... voids) {

            try {
                Response response = client.newCall(request).execute();
                System.out.println(response.body().string());
                builder = new AlertDialog.Builder();
                TimeUnit.SECONDS.sleep(3);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            catch (IOException e){
                e.printStackTrace();
            }

            return null;
        }

        @Override
        protected void onPostExecute(Void aVoid) {
            super.onPostExecute(aVoid);
            startActivity(new Intent(Splash.this, MainActivity.class));
            finish();
        }
    }
}

