<template>
  <div class="contact-list">
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <th class="text-left">Name</th>
          <th class="text-left">Last Name</th>
          <th class="text-left">Phone</th>
          <th>Edit</th>
        </thead>
        <tbody>
          <tr v-for="contact in contacts" :key="contact.id">
            <td>{{contact.name}}</td>
            <td>{{contact.last_name}}</td>
            <td>{{contact.phone}}</td>
            <td></td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>

</template>


<script>
    import axios from 'axios'
    export default {
        name: 'ContactsList',
        data: () => {
          return {
          contacts: []
          }
        },
      mounted() {
        axios.get('/api/contacts/all')
          .then(data => {
            this.contacts = data.data;
          })
      }
    }
</script>
