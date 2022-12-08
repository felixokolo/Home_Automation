package com.example.agile_control;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import java.io.IOException;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.TimeUnit;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

	Button loginButton;
	EditText usernameBox;

	@SuppressLint("MissingInflatedId")
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		loginButton = (Button) findViewById(R.id.login_button);
		usernameBox = (EditText) findViewById(R.id.usernameBox);
		usernameBox.setOnFocusChangeListener(new View.OnFocusChangeListener() {
			@Override
			public void onFocusChange(View view, boolean b) {
				if (b){
					usernameBox.getText().clear();
					usernameBox.setTextColor(ContextCompat.getColor(getApplicationContext(), R.color.black));
				}
			}
		});
	}

	public void login_button_action(View view){
		if (view.getId() == R.id.login_button){
			String username = usernameBox.getText().toString();
			String url = getResources().getString(R.string.ip_url) + username;
			String resp = "null";
			try {
				resp = new ConnectionSetup().execute(url).get();
			} catch (ExecutionException e) {
				e.printStackTrace();
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			//AlertDialog.Builder builder = new AlertDialog.Builder(this);
			//builder.setMessage(resp);
			//builder.setTitle("Json response");
			//AlertDialog dialog = builder.create();
			//dialog.show();
			if (resp != "null"){
				Intent intent = new Intent(MainActivity.this, User.class);
				Bundle b = new Bundle();
				b.putString("json", resp);
				intent.putExtras(b);
				startActivity(intent);
			}
		}

		if (view.getId() == R.id.usernameBox){

		}
	}
}

