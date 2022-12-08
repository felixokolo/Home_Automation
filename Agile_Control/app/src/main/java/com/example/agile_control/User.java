package com.example.agile_control;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class User extends AppCompatActivity {

	TextView jsontext;
	RecyclerView recyclerView;
	ChannelListAdapter adapter;
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_user);
		Bundle b = getIntent().getExtras();
		String text = b.getString("json");
		JSONObject arr = null;
		recyclerView
				= (RecyclerView)findViewById(
				R.id.recyclerView);
		ClickListiner listiner = null;
		//jsontext = (TextView) findViewById(R.id.channelName);
		List<ChannelData> channels = new LinkedList<ChannelData>();
		JSONArray jsonChannels = null;
		try {
			jsonChannels = new JSONArray(text);
		} catch (JSONException e) {
			e.printStackTrace();
		}
		if (jsonChannels != null) {
			try {
				Iterator<String> k;
				JSONArray ch;
				for (int i = 0; i < jsonChannels.length(); i++){
					arr = jsonChannels.getJSONObject(i);
					k = arr.keys();
					while (k.hasNext()){
						ch = arr.getJSONArray(k.next());
						for (int j =0; j < ch.length(); j++){
							channels.add(new ChannelData(ch.getJSONObject(j)));
						}
					}
				}
			} catch (JSONException e) {
				e.printStackTrace();
			}

		}
		adapter
				= new ChannelListAdapter(
				channels, getApplication(),listiner);
		recyclerView.setAdapter(adapter);
		recyclerView.setLayoutManager(
				new LinearLayoutManager(User.this));
	}
}